from sqlalchemy import inspect

from model.user import db


# 评论表（评论id，评论用户id，评论用户名称，评论用户头像，父评论id（顶层为0），文章id，
# 文章标题，评论时间）
class Comment(db.Model):
    #  '评论id',
    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # '评论用户id',
    user_id = db.Column(db.Integer, nullable=False)
    # '父评论id（顶层为0）',
    comment_parent_id = db.Column(db.Integer, nullable=False, default='0')
    # '文章id',
    article_id = db.Column(db.Integer, nullable=False)
    # 回复的用户id
    be_comment_user_id = db.Column(db.Integer)
    # '评论内容'
    com_content = db.Column(db.String(120), nullable=False)
    # '评论时间'
    comment_time = db.Column(db.DATETIME, default='null')

    def __init__(self, comment_id, user_id,
                 comment_parent_id, article_id, comment_time, com_content,
                 be_comment_user_id):
        self.comment_id = comment_id
        self.user_id = user_id
        self.comment_parent_id = comment_parent_id
        self.article_id = article_id
        self.comment_time = comment_time
        self.com_content = com_content
        self.be_comment_user_id = be_comment_user_id

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
