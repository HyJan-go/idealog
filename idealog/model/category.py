from sqlalchemy import inspect

from model.user import db


# 分类表（分类id，父分类id，分类名称）
class Category(db.Model):
    # 分类id
    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # '分类名称'
    cate_name = db.Column(db.String(15), nullable=False)

    def __init__(self, category_id, cate_name):
        self.category_id = category_id
        self.cate_name = cate_name

    def __repr__(self):
        return '<category_id %r>' % self.category_id

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
