from flask import jsonify
from flask import request, Blueprint

from model.article import Article
from model.user import User

find = Blueprint('find', __name__)


# get

@find.route("/find", methods=['POST', 'GET'])
def find_key():
    datas = request.get_json()
    title = datas["title"]
    all_results = Article.query.filter(Article.title.like("%" + title + "%") if title is not None else "").all()
    result = []
    for article in all_results:
        user = User.query.filter(User.id == article.user_id).first()
        result.append({
            "article_id": article.article_id,
            "category_id": article.category_id,
            "category_name": article.category_name,
            "comment_num": article.comment_num,
            "content": article.content,
            "content_pic": article.content_pic,
            "enclosure_addr": article.enclosure_addr,
            "fabulous_num": article.fabulous_num,
            "send_time": str(article.send_time),
            "tag_id": article.tag_id,
            "tag_name": article.tag_name,
            "title": article.title,
            "update_time": str(article.update_time),
            "user_id": article.user_id,
            "user_name": user.nick_name,
            "look_num": article.look_num
        })
    return jsonify({"status": "200", "msg": "ok", "result": result})
