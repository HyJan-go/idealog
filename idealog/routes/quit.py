from flask import request, Blueprint, jsonify

from common.commons import get_redis_cli, get_user_id_by_cookie, is_user_login, is_admin_login, get_admin_id_by_cookie

quit = Blueprint('quit', __name__)


# 用户退出登录，删除用户在redis的存储信息
@quit.route("/user/quit", methods=['POST'])
def user_quit():
    redis = get_redis_cli()
    if not is_user_login(request):
        return jsonify({'code': 208, 'msg': '用户信息已过期'})
    user_id = get_user_id_by_cookie(request)
    uuid = redis.get("user:" + str(user_id))
    redis.delete("user:" + str(user_id))
    redis.delete("user:" + str(uuid))
    return jsonify({'code': 200, 'msg': '用户退出成功'})


# 管理员退出登录，删除管理员在redis的存储信息
@quit.route("/admin/quit", methods=['POST'])
def admin_quit():
    redis = get_redis_cli()
    if not is_admin_login(request):
        return jsonify({'code': 208, 'msg': '管理员信息已过期'})
    uuid = request.cookies.get('admin_token')
    redis.delete("admin:" + str(uuid))
    return jsonify({'code': 200, 'msg': '管理员退出成功'})
