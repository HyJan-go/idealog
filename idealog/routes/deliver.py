import time

from flask import request, jsonify, Blueprint

from common.commons import exist_user, exist_category, is_user_login, get_user_id_by_cookie
from model.article import Article, db
from model.user import User
from model.tag import Tag
deliver = Blueprint('deliver', __name__)


# get


@deliver.route("/deliver", methods=['POST'])
def deliver_article():
    data = request.get_json()
    if is_user_login(request):
        user_id = get_user_id_by_cookie(request)
    else:
        return jsonify({'code': 208, 'msg': "登录信息已经过期"})
    reward_status = int(data['reward_status'])
    title = data['title']
    content = data['content']
    tag_id = data['tag_id']
    category_id = data['category_id']
    category_name = data['category_name']
    tag_name = data['tag_name']
    if exist_user(user_id) and exist_category(category_id):
        send_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        if title == '' or title.isspace():
            title = None
        if content == '' or content.isspace():
            content = None
        r1 = Article(user_id, title, content, tag_id, category_id, tag_name, send_time, send_time,
                     category_name, reward_status)
        try:
            db.session.add(r1)
            # 作者发布文章，+3积分
            user = User.query.filter(User.id == user_id).first()
            user.effect += 4
            tag_id =str(tag_id)
            ids =tag_id.split(",")
            for i in  ids :
                result=Tag.query.filter(Tag.tag_id == i).first()
                result.tag_heat=int(result.tag_heat) + int(1)
            db.session.commit()
            #print('user.effect:', user.effect)
            return jsonify({"status": "200", "msg": "发布成功"})
        except:
            db.session.rollback()
            return jsonify({"status": "203", "msg": "发布失败"})
    else:
        return jsonify({"status": "203", "msg": "参数有误"})
