# 配置文件
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root1234@192.168.195.10:3306/idealog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

url_default_Avatar = 'http://192.168.195.10:5005/user/images/default.png'
admin_url_default_Avatar = 'http://192.168.195.10:5005/admin/images/default.jpg'

redis_host = "192.168.195.10"
redis_port = "6379"
redis_password = "foo"
