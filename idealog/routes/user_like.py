import time

from flask import Blueprint, jsonify, request

from model.fabulous import Fabulous, db
from model.article import Article
from common.commons import exist_user, is_user_login, get_user_id_by_cookie
from model.notice import Notice
from model.user import User
from common.commons import get_redis_cli
like_article = Blueprint('like_article', __name__)


# get

# 已经点赞?
# --是
#   --点赞：提示你已经赞过了
#   --取消：文章表赞数-1，点赞表状态置为0
# --否
#   --点赞：文章表赞数+1，点赞表状态置为1，推送
#   --取消：返回203 响应成功
#   第一次点赞完成：1
#   取消了0
#   再点：-1

@like_article.route('/like', methods=['POST'])
def like():
    data = request.get_json()
    # 参数：用户id 文章id 点赞状态 点赞数(?)
    if not is_user_login(request):
        return jsonify({"code": 208, "msg": "登录信息已经过期"})
    user_id = get_user_id_by_cookie(request)
    if not exist_user(user_id):
        return {"code": 201, "msg": "用户不存在"}
    article_id = int(data['article_id'])
    # action == 0 -> 取消点赞, 1 -> 点赞
    action = int(data['like_action'])
    redis = get_redis_cli()
    time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 是否已经点赞
    liked = db.session.query(Fabulous).filter_by(user_id=user_id, article_id=article_id).first()
    article = db.session.query(Article).filter_by(article_id=article_id).first()
    if article is None:
        # 并没有该文章, 报错
        return jsonify({"code": 500, "msg": "该文章不存在"})
    # 作者id
    author_id = article.user_id
    if not exist_user(author_id):
        return {"code": 203, "msg": "作者不存在"}
    author = User.query.filter(User.id == author_id).first()
    # 用户
    user = User.query.filter(User.id == user_id).first()
    notice_title = "你有新的一条点赞信息"
    notice_content = "用户：" + str(user.nick_name) + "点赞了你的文章：" + str(article.title)
    status_key = "status:" + "like:" + str(article.user_id)
    result = Notice.query.filter(Notice.user_id == author_id, Notice.initiative_id == user_id,
                                 Notice.sort == '1').first()
    if liked is not None:
        if action == 1:
            if liked.fabulous_status == 0:
                liked.fabulous_status = -1
                article.fabulous_num += 1
                # 有人点赞，作者+1积分
                author.effect += 2
                # 点赞，个人+1积分
                user.effect += 1
                db.session.commit()
                like_count = db.session.query(Article).filter_by(article_id=article_id).first().fabulous_num
                # 发送推送
                # 找出被点赞的文章作者的id
                # 点赞热度文章加3
                article.heat = int(article.heat) + int(3)
                if result is None:
                   n1 = Notice(None, article.user_id, notice_title, notice_content, 0, time1, -1, 1,user_id)
                   db.session.add(n1)
                else:
                   result.notice_content = "用户：" + str(user.nick_name) + "点赞了你的文章：" + str(article.title)
                db.session.commit()
                if redis.keys(status_key):
                    redis.incr(status_key)
                else:
                    redis.set(status_key, 1)
                return jsonify({"code": 200, "msg": "点赞成功", "like_count": like_count})
            return jsonify({"code": 204, "msg": "已经点过赞"})
        else:
            if liked.fabulous_status == 1 or liked.fabulous_status == -1:
                article.fabulous_num -= 1
                liked.fabulous_status = 0
                # 有人取消点赞，作者-1积分
                author.effect -= 2
                # 取消点赞，个人-1积分
                user.effect -= 1
                article.heat -= 3
                db.session.commit()
                redis_result=redis.get(status_key)
                if int(redis_result) == 1 :
                    redis.delete(status_key)
                if int(redis_result) > 1:
                    redis.decr(status_key)
            return jsonify({"code": 205, "msg": "取消点赞成功"})
    else:
        if action == 1:
            new_like = Fabulous(None, user_id=user_id, article_id=article_id,
                                fabulous_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), fabulous_status=1)
            db.session.add(new_like)
            article.fabulous_num += 1
            #  有人点赞，作者+1积分
            author.effect += 2
            db.session.commit()
            like_count = db.session.query(Article).filter_by(article_id=article_id).first().fabulous_num
            # TODO 发推送
            # 点赞热度文章加3
            article.heat = int(article.heat) + int(3)
            if result is None:
                n1 = Notice(None, article.user_id, notice_title, notice_content, 0, time1, -1, 1, user_id)
                db.session.add(n1)
            else:
                result.notice_content = "用户：" + str(user.nick_name) + "点赞了你的文章：" + str(article.title)
            db.session.commit()
            if redis.keys(status_key):
                redis.incr(status_key)
            else:
                redis.set(status_key, 1)
        else:
            return jsonify({"code": 203, "msg": "没有点赞无法取消点赞"})

    return jsonify({"code": 200, "msg": "点赞成功", "like": like_count})
