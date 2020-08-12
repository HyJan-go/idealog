from sqlalchemy import inspect

from model.user import db


# 标签表
class Tag(db.Model):
    # 标签id
    tag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 标签名称
    tag_name = db.Column(db.String(15), nullable=False)
    # 标签热度
    tag_heat = db.Column(db.Integer, default='0')

    def __init__(self, tag_id, tag_name, tag_heat):
        self.tag_id = tag_id
        self.tag_name = tag_name
        self.tag_heat = tag_heat

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
