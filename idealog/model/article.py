from sqlalchemy import inspect

from model.user import db


# 文章表
class Article(db.Model):
    # 文章id
    article_id = db.Column(db.Integer, primary_key=True,
                           autoincrement=True)
    # 用户id（发表者）
    user_id = db.Column(db.Integer, nullable=False)
    # 附件地址
    enclosure_addr = db.Column(db.String(100), default=None)
    # 文章标题
    title = db.Column(db.String(35), nullable=False)
    # 文章内容
    content = db.Column(db.Text, nullable=False)
    # 文章带着的图片地址
    content_pic = db.Column(db.String(100), default=None)
    # 发表时间
    send_time = db.Column(db.DATETIME, default=None)
    # 更新时间
    update_time = db.Column(db.DATETIME, default=None)
    # 标签id
    tag_id = db.Column(db.String(15), nullable=False)
    # 分类id
    category_id = db.Column(db.Integer, nullable=False)
    # 标签名称
    tag_name = db.Column(db.String(60), nullable=False)
    # 分类名
    category_name = db.Column(db.String(15), default=None)
    # 点赞数
    fabulous_num = db.Column(db.Integer, default='0')
    # 评论数（所有与文章相关的评论和回复都算）
    comment_num = db.Column(db.Integer, default='0')
    # 浏览数
    look_num = db.Column(db.Integer, default='0')
    # 是否放打赏图片(1 表示放，0 表示不放) 默认就是放的
    reward_status = db.Column(db.Boolean, default='1')

    heat=db.Column(db.Integer)

    def __init__(self, user_id, title, content, tag_id, category_id, tag_name, update_time, send_time,
                 category_name,reward_status='1', heat='0',fabulous_num='0', comment_num='0',article_id=None,
                 enclosure_addr=None, content_pic=None, look_num='0'):
        self.article_id = article_id
        self.user_id = user_id
        self.title = title
        self.content = content
        self.enclosure_addr = enclosure_addr
        self.content_pic = content_pic
        self.send_time = send_time
        self.update_time = update_time
        self.tag_id = tag_id
        self.category_id = category_id
        self.tag_name = tag_name
        self.category_name = category_name
        self.fabulous_num = fabulous_num
        self.comment_num = comment_num
        self.look_num = look_num
        self.reward_status = reward_status
        self.heat =heat
    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
