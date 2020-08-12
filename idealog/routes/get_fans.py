from flask import request, jsonify, Blueprint

from common.commons import is_user_login, get_user_id_by_cookie
from model.follow import Follow
from model.user import User

fans_list = Blueprint('getFans', __name__)


# get

# author:陈樱脡  获取粉丝列表
@fans_list.route('/get_fans', methods=['POST'])
def get_fans():
    if not is_user_login(request):
        return jsonify({"code": 208, "msg": "登录信息已经过期"})
    # 拿到当前登录者id
    self_id = get_user_id_by_cookie(request)
    myself = User.query.filter(User.id == self_id).first()
    # 查看粉丝
    data = request.get_json()
    user_id = data["user_id"]
    user = User.query.filter(User.id == user_id).first()
    if user:
        return query_follow(user_id, myself)
    else:
        return jsonify({'code': 203, 'msg': "user_id does't exit"})


def query_follow(user_id, myself):
    # 查询有哪些人关注了他
    user = Follow.query.filter(Follow.followed_id == user_id).all()
    fans_list = []
    for i in user:
        # 根据Follow表的user_id去匹配User表的id，得到粉丝信息
        fans = User.query.filter(User.id == i.user_id).first()
        if fans is None:
            return jsonify({'code': 203, 'msg': "fans does't exit"})
        else:
            # 查询是否相互关注，被关注者作为主动关注者，粉丝作为被关注者，查询Follow，有记录则将'back_status'设为1，表示相互关注
            # fo = Follow.query.filter(user_id == Follow.user_id, Follow.followed_id == i.user_id).first()
            # 自己对粉丝的关注状态
            fo_1 = Follow.query.filter(Follow.user_id == myself.id, Follow.followed_id == i.user_id).first()
            # 查询粉丝对自己的关注状态
            fo_2 = Follow.query.filter(Follow.user_id == i.user_id, Follow.followed_id == myself.id).first()
            if fo_1 is None:
                # 自己没有关注粉丝
                back_status = 0
            else:
                if fo_2 is None:
                    # 自己关注粉丝，粉丝没有关注自己
                    back_status = 2
                else:
                    # 互粉
                    back_status = 1
            fans_list.append({
                'user_id': fans.id,
                'nick_name': fans.nick_name,
                'avatar': fans.avatar,
                'back_status': back_status
            })

    return jsonify(fans_list)
