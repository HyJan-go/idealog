from sqlalchemy import inspect
from flask_sqlalchemy import SQLAlchemy
from conf import app, url_default_Avatar

db = SQLAlchemy(app)


# 用户表
class User(db.Model):
    # 用户id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 用户昵称
    nick_name = db.Column(db.String(15))
    # 工号
    work_id = db.Column(db.String(10), nullable=False, unique=True)
    # 联系方式
    tel = db.Column(db.String(15), default=None)
    # 1-男，0-女
    gender = db.Column(db.Integer, default='1')
    # 密码
    passwd = db.Column(db.String(64), nullable=False)
    # 头像地址
    avatar = db.Column(db.String(100), default=url_default_Avatar)
    # 邮箱
    mail = db.Column(db.String(32), unique=True)
    # 虚拟货币数
    vir_money = db.Column(db.Integer, default=50)
    # 关注数
    follow = db.Column(db.Integer, default='0')
    # 被关注数
    followers = db.Column(db.Integer, default='0')
    # 自我介绍
    profile = db.Column(db.String(150), default=None)
    # 打赏图片
    reward_addr = db.Column(db.String(100), default=None)
    # 影响力
    effect = db.Column(db.Integer, default=0)
    # 0-正常，1-离职，-1-注销
    status = db.Column(db.Integer, default='0')
    # 是否为第一次登陆(1 表示是第一次登陆， 0表示今天已经登陆过了)
    first_login = db.Column(db.INT, default=1)

    def __init__(self, work_id, passwd, avatar=url_default_Avatar):
        self.work_id = work_id
        self.passwd = passwd
        self.avatar = avatar

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
