from flask import request, jsonify, Blueprint

from common.commons import get_redis_cli
from model.user import User, db

del_user = Blueprint('del_user', __name__)


# get

# author: wuchuming
# 获取token登录信息，判断是否为管理员
# 管理员删除用户(逻辑删除，更新用户状态，文章保留)
# 更新redis缓存
@del_user.route('/ad/del_user', methods=['GET'])
def delete_user():
    uid = request.cookies.get('admin_token')
    if uid is not None:
        redis = get_redis_cli()
        if redis.ttl("admin:" + str(uid)) <= 0:
            return jsonify({'code': 208}, {'msg': 'try login again'})
        user_id = request.args.get("user_id")
        user = set_user_status(user_id)
        if user is not None:
            update_redis(user, redis)
            return jsonify({'code': 200}, {'msg': "success"})
        return jsonify({'code': 203, 'msg': "user doesn't exit"})
    else:
        return jsonify({'code': 208, 'msg': "please login"})


# author: wuchuming
# 设置用户状态为离职
def set_user_status(user_id):
    user = db.session.query(User).get(user_id)
    if user is not None:
        user.status = 1
        db.session.commit()
    return user


# author: wuchuming
# 如果redis缓存有该用户信息，更新之
# Fix me: 如何更好实现读写分离      
# update: HyJan
# Q: 删除了用户，为什么要更新redis呢，删除就可以了,而且上面好像并不用判断，为什么要返回true呢
# update: wuchuming
# A: 不直接删除redis有一些考虑，如果某处的逻辑是员工能否登录或者获取信息会依据员工状态判断，
# 那么员工离职后实际上并不应该立刻不能够访问系统个人信息，留一些善后时间比较合理。或者不然，也应该在其他方面做一些通知。
def update_redis(result, redis):
    uuid = redis.get("user:" + str(result.id))
    redis.delete("user:" + str(result.id))
    redis.delete("user:" + str(uuid))

    # time_to_live = redis.ttl("user:" + str(result.id))
    # if time_to_live > 0:
    #     uid = redis.get("user:" + str(result.id))
    #     list = {"id": result.id, "nick_name": result.nick_name, "work_id": result.work_id,
    #             "tel": result.tel, "gender": result.gender,
    #             "avatar": result.avatar, "mail": result.mail, "vir_money": result.vir_money,
    #             "follow": result.follow, "followers": result.followers, "profile": result.profile,
    #             "reward_addr": result.reward_addr, "effect": result.effect, "status": result.status}
    #     # Fix me: 如何更新对应值而不重置生存时间
    #     redis.set("user:" + str(uid), str(list), time_to_live)
    # return True
