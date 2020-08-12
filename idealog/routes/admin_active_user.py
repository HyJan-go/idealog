from flask import request, jsonify, Blueprint

from common.commons import get_redis_cli
from model.user import User, db

active_user = Blueprint('active_user', __name__)


# author: wuchuming
# 获取token登录信息，判断是否为管理员
# 管理员激活用户
@active_user.route('/ad/active_user', methods=['GET'])
def dactive_user():
    uid = request.cookies.get('admin_token')
    if uid is not None:
        redis = get_redis_cli()
        if redis.ttl("admin:" + str(uid)) <= 0:
            return jsonify({'code': 208, 'msg': 'try login again'})
        user_id = request.args.get("user_id")
        user = set_user_status(user_id)
        if user is not None:
            return jsonify({'code': 200, 'msg': "success"})
        return jsonify({'code': 203, 'msg': "user doesn't exit"})
    else:
        return jsonify({'code': 208, 'msg': "please login"})


# author: wuchuming
# 激活用户状态
def set_user_status(user_id):
    user = db.session.query(User).get(user_id)
    if user is not None:
        user.status = 0
        db.session.commit()
    return user
