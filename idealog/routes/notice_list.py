from flask import Blueprint, request, jsonify

from common.commons import get_redis_cli, exist_user, is_user_login, get_user_id_by_cookie
from model.notice import Notice, db

notice_list = Blueprint('notice_list', __name__)


# ---author-mc
@notice_list.route("/notice_list", methods=['POST'])
def notice():
    data = request.get_json()
    sort = data['sort']
    if not is_user_login(request):
        return jsonify({"code": 208, "msg": "登录信息已经过期"})
    user_id = get_user_id_by_cookie(request)
    if exist_user(user_id):
        arr = []
        redis = get_redis_cli()
        if sort == "0":
            #  状态为0的话，表示查看关注列表
            result = Notice.query.filter(Notice.user_id == user_id, Notice.sort == sort).all()
            status_key = "status:" + "concern:" + str(user_id)
            redis.delete(status_key)
            for e in result:
                arr.append({
                    "notice_title": e.notice_title,
                    "notice_content": e.notice_content,
                    "notice_time": str(e.notice_time),
                    "notice_status": e.notice_status,
                    "sort":sort
                })
                # -1未读 0已读
                if e.notice_status == -1:
                    e.notice_status = 0
                    db.session.commit()
        if sort == "2":
            result = Notice.query.filter(Notice.user_id == user_id, Notice.sort == sort).all()
            status_key = "status:" + "comment:" + str(user_id)
            redis.delete(status_key)
            for e in result:
                arr.append({
                    "notice_title": e.notice_title,
                    "notice_content": e.notice_content,
                    "notice_time": str(e.notice_time),
                    "notice_status": e.notice_status,
                    "sort": sort
                })
                if e.notice_status == -1:
                    e.notice_status = 0
                    db.session.commit()
        if sort == "1":
            result = Notice.query.filter(Notice.user_id == user_id, Notice.sort == sort).all()

            status_key = "status:" + "like:" + str(user_id)
            redis.delete(status_key)
            for e in result:
                arr.append({
                    "notice_title": e.notice_title,
                    "notice_content": e.notice_content,
                    "notice_time": str(e.notice_time),
                    "notice_status": e.notice_status,
                    "sort": sort
                })
                if e.notice_status == -1:
                    e.notice_status = 0
                    db.session.commit()
        return jsonify(arr)
    else:
        return jsonify({"code": "203", "msg": "用户不存在"})
