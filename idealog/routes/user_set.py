import hashlib
import json

import sqlalchemy
from flask import Blueprint, jsonify
from flask import request

from common.commons import is_admin_login
from model.user import User, db

setUser = Blueprint('setUser', __name__)

# get


@setUser.route('/setUser', methods=['GET', 'POST'])
def get():
    work_id_data = request.get_data()
    if not is_admin_login(request):
        return jsonify({"code": 208, "msg": "登录信息已经过期"})
    user_list = json.loads(work_id_data)
    for i in range(len(user_list)):
        work_id = user_list[i].get("work_id")
        if work_id is None:
            return {"code": 203, "msg": "参数错误"}
        user = User(passwd=my_md5("123456"), work_id=work_id)
        try:
            db.session.add(user)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            # 重复插入错误处理
            db.session.remove()
            continue

    return {"code": 200, "msg": "success"}


def my_md5(s):
    m = hashlib.md5()
    m.update(s.encode(encoding='utf-8'))
    pwd = m.hexdigest()
    salt = 'abcTT'
    pwd = pwd + salt
    m = hashlib.md5(str(pwd).encode())
    return m.hexdigest()

