import time

from flask import Blueprint, jsonify, request

from common.commons import exist_user, exist_tag, exist_category, get_user_id_by_cookie, is_user_login
from model.article import Article
from model.category import Category, db
from model.tag import Tag

update_article = Blueprint('update_article', __name__)


# get

@update_article.route('/update_article', methods=['POST'])
def update():
    data = request.get_json()
    if not is_user_login(request):
        return jsonify({"code": 208, "msg": "登录信息已经过期"})
    user_id = get_user_id_by_cookie(request)
    article_id = int(data['article_id'])
    title = data['title']
    content = data['content']
    tag_id = data['tag_id']
    # 形如"1,2,3"的str
    category_id = int(data['category_id'])

    if not exist_user(user_id):
        return jsonify({"code": 204, "msg": "用户不存在"})
    if not exist_tag(tag_id):
        return jsonify({"code": 205, "msg": "标签不存在"})
    if not exist_category(category_id):
        return jsonify({"code": 206, "msg": "分类不存在"})
    article = db.session.query(Article).filter_by(article_id=article_id).first()
    if article is None:
        return jsonify({"code": 201, "msg": "文章不存在"})

    if article.user_id != user_id:
        return jsonify({"code": 202, "msg": "你不是该文章的作者"})

    # 形如linux-go-docker的字符串
    tag_name, success = split_id_str_to_name(tag_id)
    if not success:
        return jsonify({"code": 203, "msg": "标签参数有误"})

    article.tag_name = tag_name
    article.title = title
    article.content = content
    article.tag_id = tag_id
    article.category_id = category_id
    category = (db.session.query(Category)
                .filter_by(category_id=category_id).first())
    if category is None:
        article.category_name = None
    else:
        article.category_name = category.cate_name
    article.update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    db.session.commit()
    return jsonify({"code": "200", "msg": "更新成功"})


def split_id_str_to_name(tag_id_str):
    try:
        res = ""
        tag_list = tag_id_str.split(",")
        for i in range(len(tag_list)):
            res += db.session.query(Tag).filter_by(tag_id=int(tag_list[i])).first().tag_name
            if i != len(tag_list) - 1:
                res += "-"
    except Exception:
        return None, False
    return res, True
