import time

from flask import request, Blueprint, jsonify

from common.commons import exist_user, is_user_login, get_user_id_by_cookie
from common.commons import get_redis_cli
from model.follow import Follow
from model.notice import Notice
from model.user import User, db

follow = Blueprint('follow', __name__)


# get

@follow.route("/follow", methods=['GET', 'POST'])
def user_follow():
    data = request.get_json()
    if is_user_login(request):
        user_id = get_user_id_by_cookie(request)
    else:
        return jsonify({'code': 208, 'msg': "登录信息已经过期"})
    followed_id = data['followed_id']
    # concern为空表示还未关注，关系表无记录
    if exist_user(user_id) and exist_user(followed_id):
        redis = get_redis_cli()
        time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        concern = Follow.query.filter(Follow.user_id == user_id, Follow.followed_id == followed_id).first()
        status_key = "status:" + "concern:" + str(followed_id)
        user = User.query.filter(User.id == user_id).first()
        notice_title = "你收到一条关注信息拉"
        notice_content = str(user.nick_name) + "关注你了"
        result = Notice.query.filter(Notice.user_id == followed_id, Notice.initiative_id == user_id,
                                     Notice.sort == '0').first()
        if result is None:
            n1 = Notice(None, followed_id, notice_title, notice_content, 0, time1, -1, 0, user_id)
            db.session.add(n1)
        else:
            re = Notice.query.filter(Notice.initiative_id == user_id, Notice.sort == '0')
            for e in re:
                e.notice_content = str(user.nick_name) + "关注你了"
        db.session.commit()
        if concern is None:
            r1 = Follow(user_id, followed_id)
            user.follow = user.follow + 1
            # 关注别人，个人积分+1
            user.effect += 1
            usered = User.query.filter(User.id == followed_id).first()
            usered.followers = usered.followers + 1
            # 有人关注，作者积分+5
            usered.effect += 5
            db.session.commit()
            try:
                db.session.add(r1)
                db.session.commit()
                if redis.keys(status_key):
                    redis.incr(status_key)
                else:
                    redis.set(status_key, 1)
                return jsonify({"msg": "1", "code": "这个是关注成功"})
            except:
                db.session.rollback()
                return jsonify({"msg": "0", "code": "这个是关注失败"})
        else:
            try:
                db.session.delete(concern)
                db.session.commit()
                user.follow = user.follow - 1
                # 取关，个人积分-1
                user.effect -= 1
                db.session.commit()
                usered = User.query.filter(User.id == followed_id).first()
                usered.followers = usered.followers - 1
                # 有人取消关注，作者积分-5
                usered.effect -= 5
                db.session.commit()
                redis_result = redis.get(status_key)
                if int(redis_result) == 1:
                    redis.delete(status_key)
                if int(redis_result) > 1:
                    redis.decr(status_key)
                return jsonify({"msg": "0", "code": "这个是取消关注成功"})
            except:
                db.session.rollback()
                return jsonify({"msg": "1", "code": "这个是取消关注失败"})
    return jsonify({'code': 203, 'msg': "user does't exit"})
