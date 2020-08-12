from flask import request, Blueprint, jsonify

# author: wuchuming
# 分页查询
# 返回json(key:序号, value:用户json)
from common.commons import is_admin_login
from model.user import User, db
from sqlalchemy import func

user_list = Blueprint('user_list', __name__)


@user_list.route('/user_list_slice', methods=['POST'])
def user_list_slice():
    data = request.get_json()
    if not is_admin_login(request):
        return jsonify({"code": 208, "msg": "登录信息已经过期"})
    page_index = data['pageIndex']
    if int(page_index) <= 0:
        return jsonify([])
    page_size = 15
    query = db.session.query(User)
    if 'nick_name' in data.keys():
        query = query.filter(User.nick_name.like("%" + data['nick_name'] + "%"))
    result = query.limit(page_size).offset((int(page_index) - 1) * page_size)
    return jsonify(User.serialize_list(result))


@user_list.route('/user_list_slice/search', methods=['POST'])
def user_list_search():
    return user_list_slice()

@user_list.route('/user_list_slice/get_all_page', methods=['POST', 'GET'])
def get_all_page():
    data = request.get_json()
    all_counts = 0
    query = db.session.query(func.count(User.id))
    if 'nick_name' in data.keys() and data['nick_name'] != "":
        query = query.filter(User.nick_name.like("%" + data['nick_name'] + "%"))
    all_counts = query.scalar()
    all_page = 0
    while (all_counts > 0):
        all_page += 1
        all_counts -= 15
    return jsonify({'code': 200, 'all_page': all_page})
