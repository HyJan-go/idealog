import hashlib
import time
import uuid

from flask import request, jsonify, make_response, Blueprint

from model.reward import Reward
from model.user import User, db
from common.commons import get_redis_cli

user = Blueprint('user', __name__)


# get


# 根据前端获得的账号和密码，查询数据库，匹配成功则加入redis
@user.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    account = data['user_account']
    password = data['user_password']
    user = query(account, password)
    if type(user) == type('str'):
        return jsonify({'code': 203, 'msg': "password error"})
    elif user is None:
        return jsonify({'code': 203, 'msg': "user does't exit"})
    elif user is not None:
        return token(account)


# 根据账号和密码查询数据库进行校对，正确返回200，错误返回提示信息
def query(account, password):
    account = User.query.filter(User.work_id == account, User.status == '0').first()
    if account:
        password = my_md5(password)
        pwd = User.query.filter(User.work_id == account.work_id, User.passwd == password).first()
        if pwd:
            return account
        else:
            return 'password error'
    else:
        return None


# 根据账号查询用户信息，将用户信息存进redis，并返回response信息给前端，以及返回cookie给浏览器
def token(account):
    redis = get_redis_cli()
    uid = uuid.uuid4()
    result = User.query.filter_by(work_id=account).first()
    if result.first_login == 1:
        first_login = 1
        # 先增加虚拟货币数，然后记录下来
        result.vir_money += 5
        # 添加记录
        reward_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 如果打赏用户是0，article_id 也是0, 说明是系统打赏的
        reward = Reward(result.id, result.id, 5, reward_time, 0, "系统打赏")
        db.session.add(reward)
    else:
        first_login = 0
    result.first_login = 0
    db.session.commit()
    list = {"id": result.id, "nick_name": result.nick_name, "work_id": result.work_id,
            "tel": result.tel, "gender": result.gender,
            "avatar": result.avatar, "mail": result.mail, "vir_money": result.vir_money,
            "follow": result.follow, "followers": result.followers, "profile": result.profile,
            "reward_addr": result.reward_addr, "effect": result.effect, "status": result.status}
    # key为 uid, value为 str(list), 有效期604800s
    redis.set("user:" + str(result.id), str(uid), 604800)
    redis.set("user:" + str(uid), str(list), 604800)
    response = make_response(
        jsonify({'code': 200, 'msg': 'login successfully', 'id': result.id, 'nick_name': result.nick_name,
                 "avatar": result.avatar, "effect": result.effect, "first_login": first_login}))
    response.set_cookie("token", str(uid))
    return response


def my_md5(s):
    salt = 'abcTT'
    s = s + salt
    # 创建md5对象
    # s.encode()#变成bytes类型才能加密
    m = hashlib.md5(str(s).encode())
    return m.hexdigest()
