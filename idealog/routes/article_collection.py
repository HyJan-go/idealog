import time

from flask import Blueprint, request, jsonify
from common.commons import  is_user_login,get_user_id_by_cookie
from model.article import Article
from model.collection import Collection, db
from model.user import User

article_collection = Blueprint('article_collection', __name__)


# get

@article_collection.route("/article_collection", methods=['GET', 'POST'])
def collect():
    data = request.get_json()
    if is_user_login(request):
        user_id = get_user_id_by_cookie(request)
    else:
        return jsonify({'code': 208, 'msg': "登录信息已经过期"})
    article_id = data["article_id"]
    article_result = Article.query.filter(Article.article_id == article_id).first()
    user_result = User.query.filter(User.id == user_id).first()
    collection = Collection.query.filter(Collection.user_id == user_id, Collection.article_id == article_id).first()

    if user_result is None:
        return jsonify({"code": "203", "msg": "该用户不存在"})
    if article_result is None:
        return jsonify({"code": "203", "msg": "该文章不存在"})
    if collection is None:
        collect_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        C = Collection(user_id, article_id, collect_time)
        try:
            db.session.add(C)
            db.session.commit()
            return jsonify({"code": "200", "msg": "已收藏该文章"})
        except:
            db.session.rollback()
            return jsonify({"code": "203", "msg": "收藏该文章失败"})
    else:
        try:
            db.session.delete(collection)
            db.session.commit()
            return jsonify({"code": "200", "msg": "已取消收藏该文章"})
        except:
            db.session.rollback()
            return jsonify({"code": "203", "msg": "取消收藏失败"})
