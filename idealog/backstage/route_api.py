from flask import (
    Blueprint,
    make_response)
from flask import send_from_directory
from flask_sqlalchemy import SQLAlchemy

from conf import app

USER_UPLOAD_FOLDER = './user/images'
ADMIN_UPLOAD_FOLDER = './admin/images'
ARTICLE_UPLOAD_FOLDER = './user/article'
USER_REWARD_UPLOAD_FOLDER = './user/reward'
APK_DOWNLOAD_FOLDER = './apk'
ADVERTISTMENT_FOLDER = './advertisement'

test = Blueprint('test', __name__)

# 注意点： 第一，不要在行尾进行注释，不然部署会报错
# 第二，每行不要超过80个字符，这个是开会的时候说的

# 记得先建一个空数据库mpc,不然会报找不到数据库
db = SQLAlchemy(app)


# 访问服务器上的文件（已经上传成功的文件）,用户头像访问
@test.route('/user/images/<filename>')
def get_user_image(filename):
    return send_from_directory(USER_UPLOAD_FOLDER, filename)


# 访问服务器上的文件（已经上传成功的文件）,用户打赏图片访问
@test.route('/user/reward/<filename>')
def get_user_reward(filename):
    return send_from_directory(USER_REWARD_UPLOAD_FOLDER, filename)


# 访问服务器上的文件（已经上传成功的文件）,广告图片访问
@test.route('/advertise/<filename>')
def get_advertise(filename):
    return send_from_directory(ADVERTISTMENT_FOLDER, filename)


# 访问服务器上的文件（已经上传成功的文件）,管理员头像访问
@test.route('/admin/images/<filename>')
def get_admin_image(filename):
    return send_from_directory(ADMIN_UPLOAD_FOLDER, filename)


# 访问服务器上的文件（已经上传成功的文件）,文章发图访问
@test.route('/article/images/<filename>')
def get_article_image(filename):
    return send_from_directory(ARTICLE_UPLOAD_FOLDER, filename)


# 安卓apk的下载链接
@test.route('/download/<filename>')
def get_image(filename):
    response = make_response(
        send_from_directory(APK_DOWNLOAD_FOLDER, filename.encode('utf-8').decode('utf-8'), as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
    return response
