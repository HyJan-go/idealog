from flask import Blueprint, request, jsonify

from common.commons import get_redis_cli, is_user_login, get_user_id_by_cookie
from model.user import User, db

update_information = Blueprint('update_information', __name__)


# get

# ---author-mc
@update_information.route("/update_information", methods=['POST'])
def update_in():
    data = request.get_json()
    if not is_user_login(request):
        return jsonify({"code": 208, "msg": "登录信息已经过期"})
    id = get_user_id_by_cookie(request)
    nick_name = data["nick_name"]
    # 自我介绍（简介）
    profile = data["profile"]
    mail = data["mail"]
    avatar = data["avatar"]
    tel = data["tel"]
    redis = get_redis_cli()

    user = User.query.filter(User.id == id).first()
    if user is not None:
        user.nick_name = nick_name
        user.profile = profile
        # mail为 unique
        user.mail = mail
        user.avatar = avatar
        user.tel = tel
        try:
            db.session.commit()
            salt = redis.get("user:" + str(id))
            value = {
                "id": id,
                "nick_name": nick_name,
                "profile": profile,
                "mail": mail,
                "avatar": avatar,
                "tel": tel,
                "work_id": user.work_id,
                "gender": user.gender,
                "passwd": user.passwd,
                "vir_money": user.vir_money,
                "followers": user.followers,
                "follow": user.follow,
                "profile": user.profile,
                "reward_addr": user.reward_addr,
                "effect": user.effect,
                "status": user.status
            }
            redis.set("user:" + str(salt), str(value).encode("utf-8"), 604800)
            return jsonify({"code": "200", "msg": "修改成功"})
        except:
            db.session.rollback()
            return jsonify({"code": "203"})
    else:
        # 该用户不存在
        return jsonify({"code": "203"})
