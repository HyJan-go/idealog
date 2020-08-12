from sqlalchemy import inspect

from model.user import db


# 点赞表（点赞id，用户id，点赞的文章id，点赞的文章标题，点赞时间，状态（-1-第一次点赞，
# 0-取消点赞，1-点赞））
class Fabulous(db.Model):
    # '标签id',
    fabulous_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # '用户id（收藏着）',
    user_id = db.Column(db.Integer, nullable=False)
    # '点赞的文章id',
    article_id = db.Column(db.Integer, nullable=False)
    # '点赞时间',
    fabulous_time = db.Column(db.DateTime, nullable=False)
    # '状态（-1-第一次点赞，0-取消点赞，1-点赞）'
    fabulous_status = db.Column(db.INT, nullable=False)

    def __init__(self, fabulous_id, user_id, article_id, fabulous_time,
                 fabulous_status):
        self.fabulous_id = fabulous_id
        self.user_id = user_id
        self.article_id = article_id
        self.fabulous_time = fabulous_time
        self.fabulous_status = fabulous_status

    def __repr__(self):
        return '<fabulous_id %r>' % self.fabulous_id

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
