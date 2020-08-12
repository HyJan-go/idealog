from sqlalchemy import inspect

from model.user import db


# 收藏文章表（顺序id，用户id，用户头像地址，收藏文章id，收藏文章标题，收藏时间）
class Collection(db.Model):
    # '标签id',
    collection_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # '用户id（收藏者）',
    user_id = db.Column(db.Integer, nullable=False)
    # '文章id'
    article_id = db.Column(db.Integer, nullable=False)
    # '收藏时间'
    collection_time = db.Column(db.DateTime, default='null')

    def __init__(self, user_id, article_id, collection_time):
        self.user_id = user_id
        self.article_id = article_id
        self.collection_time = collection_time

    # 提供输出接口,后期根据需要改
    def __repr__(self):
        return '<Collection_Article %r>' % self.collection_id

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
