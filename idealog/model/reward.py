from sqlalchemy import inspect

from model.user import db


# 打赏记录表
class Reward(db.Model):
    # 记录id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 打赏用户id
    user_id = db.Column(db.Integer, nullable=False)
    # 被打赏用户id
    be_reward_user_id = db.Column(db.Integer, nullable=False)
    # 打赏金额
    reward_money = db.Column(db.Integer, nullable=False)
    # 备注
    remark = db.Column(db.String(150), default=None)
    # 时间
    reward_time = db.Column(db.DATETIME, nullable=False)
    # 打赏的文章id
    article_id = db.Column(db.Integer,nullable=False)

    def __init__(self, user_id, be_reward_user_id, reward_money, reward_time, article_id, remark=None):
        self.user_id = user_id
        self.be_reward_user_id = be_reward_user_id
        self.reward_money = reward_money
        self.reward_time = reward_time
        self.article_id = article_id
        self.remark = remark

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
