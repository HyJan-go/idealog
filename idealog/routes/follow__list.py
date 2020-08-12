from flask import Blueprint, request, jsonify

from common.commons import exist_user
from common.commons import is_user_login, get_user_id_by_cookie
from model.follow import Follow
from model.user import User

follow_list = Blueprint('follow_list', __name__)


# get

# -------author --mc
@follow_list.route("/follow_list", methods=['POST'])
def list():
    if not is_user_login(request):
        return jsonify({"code": 208, "msg": "登录信息已经过期"})
    # 拿到当前登录者id
    self_id = get_user_id_by_cookie(request)
    myself = User.query.filter(User.id == self_id).first()
    data = request.get_json()
    user_id = data["user_id"]
    if exist_user(user_id):
        arr = []
        result = Follow.query.filter(Follow.user_id == user_id).all()
        for e in result:
            # 结果为空，不存在此关系
            concern = Follow.query.filter(Follow.followed_id == e.followed_id, Follow.user_id == myself.id).first()
            # 如果mysql存在此关系。a=2表示我已经关注他，但他没有关注我，1表示互关，0表示我没有关注他
            if concern is None:
                a = 0
            else:
                concern1 = Follow.query.filter(Follow.followed_id == myself.id, Follow.user_id == e.followed_id).first()
                if concern1 is None:
                    a = 2
                else:
                    a = 1
            user = User.query.filter(User.id == e.followed_id).first()
            arr.append({
                'followed_id': e.followed_id,
                'followed_name': user.nick_name,
                'followed_avatar': user.avatar,
                'back_status': a
            })
        return jsonify(arr)
