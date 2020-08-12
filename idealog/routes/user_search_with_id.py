from flask import request, Blueprint, jsonify

from common.commons import get_user_reward_num, get_user_fabulous_num
from conf import app
from model.user import User, db

user_list_id = Blueprint('user_list_id', __name__)


# get, 这个是获取他人的id，拿不到token的

# 管理员根据id查用户
@app.route('/search_user_with_id', methods=['POST'])
def search_user_with_id():
    data = request.get_json()
    id = data['uid']
    result = db.session.query(User).get(id)
    the_user = {"id": result.id, "nick_name": result.nick_name, "work_id": result.work_id,
                "tel": result.tel, "gender": result.gender, "passwd": "",
                "avatar": result.avatar, "mail": result.mail, "vir_money": result.vir_money,
                "follow": result.follow, "followers": result.followers, "profile": result.profile,
                "reward_addr": result.reward_addr, "effect": result.effect, "status": result.status,
                "reward_num": get_user_reward_num(result.id),
                "fabulous_num": get_user_fabulous_num(result.id)}
    return jsonify(the_user)
