from flask import Blueprint, jsonify, request

from model.user import User, db
from model.follow import Follow
from common.commons import get_user_reward_num, get_user_fabulous_num

get_user_profile = Blueprint('get_user_profile', __name__)


# get
# visit_user_id 访问者的用户id
# host_user_id 被访问的用户id

@get_user_profile.route('/get_user_profile', methods=['GET'])
def get_profile():
    # visit_user_id 可能为空 因为未登录的情况也可以访问用户信息
    visit_user_id = request.args.get('visit_user_id')
    host_user_id = request.args.get('host_user_id')
    if host_user_id is None:
        return jsonify({"code": "203", "msg": "参数为空"})
    # 返回：
    # 当前用户对此人的关注状态 back_status
    # 头像
    # 昵称
    # 个人简介
    # 电话
    # 邮箱
    # 打赏图片url
    host = db.session.query(User).filter_by(id=host_user_id).first()
    if host is None:
        return jsonify({"code": "201", "msg": "所查看的用户不存在"})

    back_status = False
    if (visit_user_id != -1 and
            db.session.query(Follow).filter_by(user_id=visit_user_id, followed_id=host_user_id).first() is not None):
        back_status = True
    return jsonify({"code": "200", "msg": "获取用户信息成功", "work_id": host.work_id, "back_status": back_status,
                    "avatar": host.avatar, "nick_name": host.nick_name,
                    "profile": host.profile, "tel": host.tel, "mail": host.mail, "reward_addr": host.reward_addr,
                    "follow": host.follow, "followers": host.followers,
                    "reward_num": get_user_reward_num(host_user_id),
                    "fabulous_num": get_user_fabulous_num(host_user_id),
                    "effect": str(host.effect), "vir_money": str(host.vir_money)})
