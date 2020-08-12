from sqlalchemy import inspect

from model.user import db


# 关注表
class Follow(db.Model):
    # 关注id
    follow_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 关注用户id
    user_id = db.Column(db.Integer, nullable=False)
    # 被关注用户id
    followed_id = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, followed_id, follow_id=None):
        self.follow_id = follow_id
        self.user_id = user_id
        self.followed_id = followed_id

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
