import time

from flask import request, Blueprint, jsonify
from sqlalchemy import distinct

from common.commons import exist_user, exist_article, is_user_login, get_user_id_by_cookie
from model.article import Article
from model.reward import Reward
from model.user import User, db

reward = Blueprint('reward', __name__)


# 用户打赏接口 author:HyJan
@reward.route("/reward", methods=['POST'])
def user_reward():
    data = request.get_json()
    if not is_user_login(request):
        return jsonify({"code": 208, "msg": "登录信息已经过期"})
    user_id = get_user_id_by_cookie(request)
    be_reward_user_id = data['be_reward_user_id']
    article_id = data['article_id']
    reward_money = int(data['reward_money'])
    if exist_user(user_id) and exist_user(be_reward_user_id) and exist_article(article_id):
        # 货币的添加减少部分
        user = User.query.filter(User.id == user_id).first()
        # 先判断用户是否够钱支付
        if user.vir_money >= reward_money:
            try:
                user.vir_money -= reward_money
                reward_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                article = Article.query.filter(Article.article_id == article_id).first()
                remark = "给文章(" + str(article.title) + ")打赏"
                reward_money1="-"+str(reward_money)
                reward=Reward(user_id, be_reward_user_id, reward_money1, reward_time,article_id, remark)
                db.session.add(reward)
                db.session.commit()
                user = User.query.filter(User.id == be_reward_user_id).first()
                user.vir_money += reward_money
                remark1 ="你的文章("+str(article.title)+")得到奖励"
                reward1=Reward(be_reward_user_id, user_id, reward_money,reward_time, article_id, remark1)
                db.session.add(reward1)
                db.session.commit()
                # 添加进记录表（打赏记录）
                # reward = Reward(user_id, be_reward_user_id, reward_money, reward_time, article_id, remark)
                #  TODO 发通知
                return jsonify({"code": "200", "msg": "打赏成功",
                                "reward_num": get_reward_number(article_id)})
            except:
                db.session.rollback()
                return jsonify({"code": "203"})
        else:
            return jsonify({"code": "203", "msg": "金币不足，请充值"})
    else:
        return jsonify({"code": "203", "msg": "用户或文章不存在"})


# 获取文章的打赏人数
def get_reward_number(article_id):
    result = db.session.query(distinct(Reward.user_id)).filter(Reward.article_id == article_id).all()
    return len(result)
