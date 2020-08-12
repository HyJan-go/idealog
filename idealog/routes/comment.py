import time

from flask import request, Blueprint, jsonify

from common.commons import exist_user, exist_article, exist_comment
from common.commons import get_redis_cli, is_user_login, get_user_id_by_cookie
from model.article import Article
from model.comment import Comment, db
from model.notice import Notice
from model.user import User

comment = Blueprint('comment', __name__)


# get

# 发表评论，评论回复等   author:HyJan
@comment.route("/dlr/comt", methods=['GET', 'POST'])
def send_comment():
    data = request.get_json()
    print(data)
    if is_user_login(request):
        user_id = get_user_id_by_cookie(request)
    else:
        return jsonify({'code': 208, 'msg': "登录信息已经过期"})
    article_id = data['article_id']
    comment_id = data['comment_id']
    be_comment_user_id = data['be_comment_user_id']
    com_content = data['com_content']
    redis = get_redis_cli()
    user = User.query.filter(User.id == user_id).first()
    user_name = user.nick_name
    if exist_user(user_id) and exist_article(article_id):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        comment_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if be_comment_user_id == "null":
            comment = Comment(None, user_id,
                              comment_id, article_id, comment_time, com_content, None)
            db.session.add(comment)
            # 评论文章，个人+1积分
            user = User.query.filter(User.id == user_id).first()
            user.effect += 1
            db.session.commit()
            result = Article.query.filter(Article.article_id == article_id).first()
            result.heat = int(result.heat) + int(5)
            # 找出作者的id
            author_user_id = result.user_id
            notice_content = str(user_name) + "评论了你的文章:" + str(result.title)
            notice_title = "你收到了一条评论"
            n1 = Notice(None, author_user_id, notice_title, notice_content, 0, comment_time, -1, 2, user_id)
            db.session.add(n1)
            # 有人评论，作者积分+2
            author = User.query.filter(User.id == author_user_id).first()
            author.effect += 3
            db.session.commit()
            status_key = "status:" + "comment:" + str(author_user_id)
            if redis.keys(status_key):
                print(redis.keys(status_key))
            else:
                redis.set(status_key, 1)
        else:
            if exist_user(be_comment_user_id):
                comment = Comment(None, user_id,
                                  comment_id, article_id, comment_time, com_content, be_comment_user_id)
                db.session.add(comment)
                db.session.commit()
                notice_title = "你收到了一条回复"
                notice_content = str(user_name) + "回复了你的评论"
                n1 = Notice(None, be_comment_user_id, notice_title, notice_content, 0, comment_time, -1, 2, user_id)
                db.session.add(comment)
                db.session.add(n1)
                db.session.commit()
                status_key = "status:" + "comment:" + str(be_comment_user_id)
                if redis.keys(status_key):
                    print(redis.keys(status_key))
                else:
                    redis.set(status_key, 1)
            else:
                return jsonify({"code": "203", "msg": "被评论用户不存在，无法发表此评论"})
        # 评论数加1,并更新到redis
        result = db.session.query(Article).get(article_id)
        result.comment_num = result.comment_num + 1
        db.session.commit()
        return jsonify({"code": "200", "msg": "评论成功"})
    else:
        return jsonify({"code": "203", "msg": "用户不存在，无法发表此评论"})


# 获取顶层评论，倒序排序
@comment.route("/up/comt", methods=['GET', 'POST'])
def get_up_comment():
    data = request.get_json()
    article_id = data['article_id']
    if exist_article(article_id):
        comments = Comment.query.filter(Comment.comment_parent_id == '-1',
                                        Comment.article_id == article_id).order_by(Comment.comment_time.desc()).all()
        result = to_json(comments)
        return jsonify(result)
    return jsonify({"code": "203", "msg": "文章不存在，无法获取评论"})


# 获取评论回复层,倒序排序
@comment.route("/reply", methods=['GET', 'POST'])
def get_comment():
    data = request.get_json()
    comment_id = data['comment_id']
    if exist_comment(comment_id):
        comments = Comment.query.filter(Comment.comment_parent_id == comment_id).order_by(
            Comment.comment_time.desc()).all()
        result = reply_to_json(comments)
        return jsonify(result)
    else:
        return jsonify({"code": "203", "msg": "上层评论不存在，没有回复"})


# 渲染成json
def reply_to_json(comments):
    result = []
    for comment in comments:
        print(comment.comment_time)
        user = User.query.filter(User.id == comment.user_id).first()
        user2 = User.query.filter(User.id == comment.be_comment_user_id).first()
        result.append({
            "article_id": comment.article_id,
            "com_content": comment.com_content,
            "comment_id": comment.comment_id,
            "comment_parent_id": comment.comment_parent_id,
            "comment_time": str(comment.comment_time),
            "head_pic": user.avatar,
            "user_id": comment.user_id,
            "user_name": user.nick_name,
            "be_comment_user_name": user2.nick_name,
            "be_comment_user_id": comment.be_comment_user_id
        })
    return result


# 渲染成json
def to_json(comments):
    result = []
    for comment in comments:
        print(comment.comment_time)
        user = User.query.filter(User.id == comment.user_id).first()
        result.append({
            "article_id": comment.article_id,
            "com_content": comment.com_content,
            "comment_id": comment.comment_id,
            "comment_parent_id": comment.comment_parent_id,
            "comment_time": str(comment.comment_time),
            "head_pic": user.avatar,
            "user_id": comment.user_id,
            "user_name": user.nick_name,
        })
    return result
