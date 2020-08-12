import hashlib

from flask import request, jsonify, Blueprint

from common.commons import get_redis_cli
from common.commons import is_admin_login, get_admin_id_by_cookie
from model.admin import Admin, db

ad_ud_pwd = Blueprint('ad_ud_pwd', __name__)


# get

# author:陈樱脡 管理员修改密码 update_pwd:修改后的密码  original_pwd:原密码
@ad_ud_pwd.route('/ad/update_pwd', methods=['POST'])
def update_pwd():
    data = request.get_json()
    if is_admin_login(request):
        admin_id = get_admin_id_by_cookie(request)
    else:
        return jsonify({'code': 208, 'msg': "登录信息已经过期"})
    update_pwd = data['update_pwd']
    original_pwd = data['original_pwd']
    # 根据用户id查询相关元组,如果该用户存在，继续逻辑判断，否则返回该用户不存在
    user = Admin.query.filter(Admin.admin_id == admin_id).first()
    if user:
        original_pwd = my_md5(str(original_pwd))
        # 根据传进来的id，原密码和数据库里的数据进行比较，成功继续，否则返回密码不一致
        account = Admin.query.filter(Admin.nick_name == user.nick_name, original_pwd == user.passwd).first()
        # 密码匹配成功
        if account:
            user.passwd = my_md5(str(update_pwd))
            # 新密码和旧密码一样，返回相同密码，否则将新密码提交
            if user.passwd == original_pwd:
                return jsonify({'code': 203, 'msg': "the same password"})
            else:
                db.session.commit()
                uid = request.cookies.get('admin_token')
                # 从redis里删除该用户之前的token
                redis = get_redis_cli()
                redis.delete("admin:" + str(uid))
                return jsonify({'code': 200, 'msg': "update password successfully"})
        else:
            return jsonify({'code': 203, 'msg': "Passwords are inconsistent!"})
    else:
        return jsonify({'code': 203, 'msg': "admin_id does't exit"})


def my_md5(s):
    salt = 'abcTT'
    s = s + salt
    m = hashlib.md5(str(s).encode())
    return m.hexdigest()
