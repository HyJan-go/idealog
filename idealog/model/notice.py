from sqlalchemy import inspect

from model.user import db


# 通知表（通知id，通知用户id，通知标题，通知内容，通知用户邮箱，类型【0-普通通知，
# 1-公告（发给全部用户）】，通知时间，通知状态（-1-未查看，0-已查看））
class Notice(db.Model):
    # '通知id',
    notice_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # '通知用户id',
    user_id = db.Column(db.Integer, nullable=False)
    # '通知标题',
    notice_title = db.Column(db.String(15), nullable=False)
    # '通知内容',
    notice_content = db.Column(db.Text, nullable=False)
    # '类型,0-普通通知，1-公告（发给全部用户）
    notice_type = db.Column(db.INT, default='0')
    # '通知时间'
    notice_time = db.Column(db.DateTime, nullable=False)
    # Boolean：布尔类型，映射到数据库中的是tinyint类型。
    # '通知状态（-1-未查看，0-已查看)'
    notice_status = db.Column(db.INT, nullable=False)
    sort = db.Column(db.Integer, nullable=False)
    # 点赞.关注。评论人的id
    initiative_id = db.Column(db.Integer)

    def __init__(self, notice_id, user_id, notice_title, notice_content,
                 notice_type, notice_time,
                 notice_status, sort, initiative_id, user_email=None):
        self.notice_id = notice_id
        self.user_id = user_id
        self.notice_title = notice_title
        self.notice_content = notice_content
        self.user_email = user_email
        self.notice_type = notice_type
        self.notice_time = notice_time
        self.notice_status = notice_status
        self.initiative_id = initiative_id
        self.sort = sort

    def __repr__(self):
        return '<Collection_Article %r>' % self.notice_id

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
