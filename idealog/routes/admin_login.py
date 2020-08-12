import hashlib
import uuid

from flask import request, jsonify, make_response, Blueprint
from common.commons import get_redis_cli

from model.admin import Admin

login = Blueprint('login', __name__)


# get

# 根据前端获得的账号和密码，查询数据库，匹配成功则加入redis
@login.route('/ad/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    account = data['admin_name']
    password = data['password']
    admin = query(account, password)
    if type(admin) == type('str'):
        return jsonify({'code': 203, 'msg': "password error"})
    elif admin is None:
        return jsonify({'code': 203, 'msg': "admin does't exit"})
    elif admin is not None:
        return token(account)


# 根据账号和密码查询数据库进行校对，正确返回200，错误返回提示信息
def query(account, password):
    account = Admin.query.filter(Admin.nick_name == account).first()
    if account:
        password = my_md5(password)
        pwd = Admin.query.filter(Admin.nick_name == account.nick_name, Admin.passwd == password).first()
        if pwd:
            return account
        else:
            return 'password error'
    else:
        return None


# 根据账号查询管理员信息，将用户信息存进redis，并返回response信息给前端，以及返回cookie给浏览器
def token(account):
    redis = get_redis_cli()
    uid = uuid.uuid4()
    result = Admin.query.filter_by(nick_name=account).first()
    list = {"id": result.admin_id, "nick_name": result.nick_name, 'head_pic': result.head_pic, 'tel': result.tel,
            'mail': result.mail}
    # key为 uid, value为 str(list), 有效期604800s
    redis.set("admin:" + str(uid), str(list), 604800)
    response = make_response(jsonify(
        {'code': 200, 'msg': 'login successfully', 'id': result.admin_id, 'nick_name': result.nick_name,
         'head_pic': result.head_pic}))
    response.set_cookie("admin_token", str(uid))
    return response


def my_md5(s):
    salt = 'abcTT'
    s = s + salt
    # 创建md5对象
    # s.encode()#变成bytes类型才能加密
    m = hashlib.md5(str(s).encode())
    return m.hexdigest()
