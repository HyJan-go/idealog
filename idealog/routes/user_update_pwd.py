import hashlib

from flask import request, jsonify, Blueprint
from common.commons import get_redis_cli, is_user_login, get_user_id_by_cookie

from model.user import User, db

ud_pwd = Blueprint('update_pwd', __name__)


# get


# 修改密码 --！陈樱脡 update_pwd:修改后的密码  original_pwd:原密码
@ud_pwd.route('/update_pwd', methods=['POST'])
def update_pwd():
    data = request.get_json()
    if not is_user_login(request):
        return jsonify({"code": 208, "msg": "登录信息已经过期"})
    user_id = get_user_id_by_cookie(request)
    update_pwd = data['update_pwd']
    original_pwd = data['original_pwd']
    # 根据用户id查询相关元组,如果该用户存在，继续逻辑判断，否则返回该用户不存在
    user = User.query.filter(User.id == user_id).first()
    if user:
        original_pwd = my_md5(str(original_pwd))
        # 根据传进来的id，原密码和数据库里的数据进行比较，成功继续，否则返回密码不一致
        account = User.query.filter(User.work_id == user.work_id, original_pwd == user.passwd).first()
        # 密码匹配成功
        if account:
            user.passwd = my_md5(str(update_pwd))
            # 新密码和旧密码一样，返回相同密码，否则将新密码提交
            if user.passwd == original_pwd:
                return jsonify({'code': 203, 'msg': "the same password"})
            else:
                db.session.commit()
                uid = request.cookies.get('token')
                # 从redis里删除该用户之前的token
                redis = get_redis_cli()
                value = redis.get("user:" + str(user_id))
                redis.delete("user:" + str(uid))
                redis.delete("user:" + str(user_id))
                redis.delete("user:" + str(value))
                return jsonify({'code': 200, 'msg': "update password successfully"})
        else:
            return jsonify({'code': 203, 'msg': "Passwords are inconsistent!"})
    else:
        return jsonify({'code': 203, 'msg': "user_id does't exit"})


def my_md5(s):
    salt = 'abcTT'
    s = s + salt
    m = hashlib.md5(str(s).encode())
    return m.hexdigest()
