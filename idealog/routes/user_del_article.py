from flask import request, jsonify, Blueprint
from common.commons import get_redis_cli, is_user_login, get_user_id_by_cookie

from model.article import Article
from model.user import User, db

del_article = Blueprint('delete_article', __name__)


# get

# 用户删除文章
@del_article.route('/delete_article', methods=['POST'])
def delete_article():
    data = request.get_json()
    if not is_user_login(request):
        return jsonify({"code": 208, "msg": "登录信息已经过期"})
    user_id = get_user_id_by_cookie(request)
    article_id = data["article_id"]
    user = User.query.filter(User.id == user_id).first()
    if user:
        article = Article.query.filter(Article.article_id == article_id, Article.user_id == user.id).first()
        return delete(article)
    else:
        return jsonify({'code': 203, 'msg': 'please login again'})


# author:陈樱脡  管理员删除文章
@del_article.route('/ad/del_article', methods=['POST'])
def get_token():
    uid = request.cookies.get('admin_token')
    redis = get_redis_cli()
    uid_redis = redis.get("admin:" + str(uid))
    if uid_redis is not None:
        data = request.get_json()
        article_id = data["article_id"]
        article = Article.query.filter(Article.article_id == article_id).first()
        return delete(article)
    else:
        return jsonify({'code': 203, 'msg': 'please login again'})


def delete(article):
    if article:
        db.session.delete(article)
        db.session.commit()
        return jsonify({'code': 200, 'msg': "delete successfully"})
    else:
        return jsonify({'code': 203, 'msg': "article does't exit"})
