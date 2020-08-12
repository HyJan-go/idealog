from flask import Blueprint, request, jsonify

from common.commons import is_user_login, get_user_id_by_cookie
from model.reward import Reward
from sqlalchemy import and_, desc

reward_list = Blueprint('reward_list', __name__)


# ---author-mc
@reward_list.route("/reward_list", methods=['POST'])
def reward_li():
    if not is_user_login(request):
        return jsonify({"code": 208, "msg": "登录信息已经过期"})
    user_id = get_user_id_by_cookie(request)
    result=Reward.query.filter(Reward.user_id==user_id).order_by(desc('reward_time')).all()
    arr = []
    for i in  result:
        arr.append({
            "reward_time" :str(i.reward_time),
            "reward_money":i.reward_money,
            'remark': i.remark
        })
    return jsonify(arr)