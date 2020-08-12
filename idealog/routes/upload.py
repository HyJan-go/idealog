import os

from flask import request, Blueprint, jsonify
from pypinyin import lazy_pinyin
from werkzeug.utils import secure_filename

from common.commons import exist_user, exist_admin, is_user_login, get_user_id_by_cookie, is_admin_login, \
    get_admin_id_by_cookie
from common.commons import get_redis_cli
from conf import app
from model.admin import Admin
from model.user import User, db

USER_UPLOAD_FOLDER = './user/images'
ADMIN_UPLOAD_FOLDER = './admin/images'
ARTICLE_UPLOAD_FOLDER = './user/article'
USER_REWARD_UPLOAD_FOLDER = './user/reward'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])
upload = Blueprint('upload', __name__)

app.config['USER_UPLOAD_FOLDER'] = USER_UPLOAD_FOLDER
app.config['ADMIN_UPLOAD_FOLDER'] = ADMIN_UPLOAD_FOLDER
app.config['ARTICLE_UPLOAD_FOLDER'] = ARTICLE_UPLOAD_FOLDER
app.config['USER_REWARD_UPLOAD_FOLDER'] = USER_REWARD_UPLOAD_FOLDER


# get

# 记得先set redis初始的唯一值，这样就可以防止名字冲突 author:HyJan

# 用户的：user-images 管理员的：admin-images 文章的： article-images 用户打赏的: user-reward


# 用户修改头像上传(尽量让名称不一样)
@upload.route('/user/pic', methods=['POST'])
def update_pic():
    file = request.files['file']
    if not is_user_login(request):
        return jsonify({"code": 208, "msg": "登录信息已经过期"})
    user_id = get_user_id_by_cookie(request)
    if exist_user(user_id):
        filename = "".join(lazy_pinyin(file.filename))
        b = "."
        redis = get_redis_cli()
        incr = redis.incr('user-images')
        filename = str(incr) + str(filename[filename.rfind(b):])
        print(filename)
        if file and allowed_file(filename):
            # 这个方法来保证文件名是安全的
            filename = secure_filename(filename)
            file.save(os.path.join(app.config['USER_UPLOAD_FOLDER'], filename))
            url = "http://192.168.195.10:5005/user/images/" + filename
            user = User.query.filter(User.id == user_id).first()
            user.avatar = url
            db.session.commit()
            return {"code": "200", "msg": "上传成功", "url": url}
        else:
            return {"code": "203", "msg": "上传失败"}
    else:
        return {"code": "203", "msg": "抱歉，用户不存在"}


# 用户打赏图片上传(尽量让名称不一样)
@upload.route('/user/reward', methods=['POST'])
def update_reward():
    file = request.files['file']
    if not is_user_login(request):
        return jsonify({"code": 208, "msg": "登录信息已经过期"})
    user_id = get_user_id_by_cookie(request)
    if exist_user(user_id):
        filename = "".join(lazy_pinyin(file.filename))
        b = "."
        redis = get_redis_cli()
        incr = redis.incr('user-reward')
        filename = str(incr) + str(filename[filename.rfind(b):])
        print(filename)
        if file and allowed_file(filename):
            # 这个方法来保证文件名是安全的
            filename = secure_filename(filename)
            file.save(os.path.join(app.config['USER_REWARD_UPLOAD_FOLDER'], filename))
            url = "http://192.168.195.10:5005/user/reward/" + filename
            user = User.query.filter(User.id == user_id).first()
            user.reward_addr = url
            db.session.commit()
            return {"code": "200", "msg": "上传成功", "url": url}
        else:
            return {"code": "203", "msg": "上传失败"}
    else:
        return {"code": "203", "msg": "抱歉，用户不存在"}


# 管理员修改头像上传 尽量让名称不一样
@upload.route('/admin/pic', methods=['POST'])
def ad_update_pic():
    file = request.files['file']
    if not is_admin_login(request):
        return jsonify({"code": 208, "msg": "登录信息已经过期"})
    admin_id = get_admin_id_by_cookie(request)
    if exist_admin(admin_id):
        filename = "".join(lazy_pinyin(file.filename))
        b = "."
        redis = get_redis_cli()
        incr = redis.incr('admin-images')
        filename = str(incr) + str(filename[filename.rfind(b):])
        if file and allowed_file(filename):
            filename = secure_filename(filename)
            file.save(os.path.join(app.config['ADMIN_UPLOAD_FOLDER'], filename))
            url = "http://192.168.195.10:5005/admin/images/" + filename
            admin = Admin.query.filter(Admin.admin_id == admin_id).first()
            admin.head_pic = url
            db.session.commit()
            return {"code": "200", "msg": "上传成功", "url": url}
        else:
            return {"code": "203", "msg": "上传失败"}
    else:
        return {"code": "203", "msg": "抱歉，管理员不存在"}


# 文章图片上传 尽量让名称不一样
@upload.route('/article/pic', methods=['POST'])
def article_pic():
    file = request.files['file']
    filename = "".join(lazy_pinyin(file.filename))
    b = "."
    redis = get_redis_cli()
    incr = redis.incr('article-images')
    filename = str(incr) + str(filename[filename.rfind(b):])
    if file and allowed_file(filename):
        filename = secure_filename(filename)
        file.save(os.path.join(app.config['ARTICLE_UPLOAD_FOLDER'], filename))
        url = "http://192.168.195.10:5005/article/images/" + filename
        # TODO  文章的部分先返回url，先不存数据库，因为可能有多张图片
        return {"code": "200", "msg": "上传成功", "url": url}
    else:
        return {"code": "203", "msg": "上传失败"}


# 判断上传的文件是不是图片格式的
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
