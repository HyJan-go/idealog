from flask import Blueprint, request, jsonify

from common.commons import get_redis_cli, exist_user, is_user_login, get_user_id_by_cookie

notice_remind = Blueprint('notice_remind', __name__)


# ---author-mc
@notice_remind.route("/notice_remind", methods=['POST'])
def notice_():
    if not is_user_login(request):
        return jsonify({"code": 208, "msg": "登录信息已经过期"})
    user_id = get_user_id_by_cookie(request)
    if exist_user(user_id):
        redis = get_redis_cli()
        status_key1 = "status:" + "concern:" + str(user_id)
        status_key2 = "status:" + "comment:" + str(user_id)
        status_key3 = "status:" + "like:" + str(user_id)
        concern_status =0
        comment_status =0
        like_status =0
        if redis.keys(status_key1):
            concern_status =1
        if redis.keys(status_key2):
            comment_status =1
        if redis.keys(status_key3):
            like_status =1
        if (concern_status ==1 or comment_status ==1 or like_status ==1) :
            return  jsonify({"code":"200","msg":"1","concern_status":concern_status,"comment_status":comment_status,"like_status":like_status})
        return  jsonify({"code":"200","msg":"0"})
    else:
        return jsonify({"code": "203", "msg": "用户不存在"})