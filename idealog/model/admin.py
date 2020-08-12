from sqlalchemy import inspect

from conf import admin_url_default_Avatar
from model.user import db


# 管理员表
class Admin(db.Model):
    # 管理员id
    admin_id = db.Column(db.Integer, primary_key=True,
                         autoincrement=True)
    # 登陆账号
    nick_name = db.Column(db.String(10), nullable=False)
    # 密码
    passwd = db.Column(db.String(64), nullable=False)
    # 头像地址
    head_pic = db.Column(db.String(100), default=None)
    # 联系方式
    tel = db.Column(db.String(15), default=None)
    # 邮箱
    mail = db.Column(db.String(32), default=None)

    def __init__(self, admin_id, nick_name, passwd, tel, mail
                 , head_pic=admin_url_default_Avatar):
        self.admin_id = admin_id
        self.nick_name = nick_name
        self.passwd = passwd
        self.head_pic = head_pic
        self.tel = tel
        self.mail = mail
        self.head_pic = head_pic

    def __repr__(self):
        return (self.admin_id + self.nick_name + self.passwd +
                self.head_pic + self.tel + self.mail)

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
