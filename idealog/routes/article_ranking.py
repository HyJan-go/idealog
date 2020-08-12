import datetime

from flask import Blueprint, request, jsonify
from sqlalchemy import and_, desc

from model.article import Article
from model.user import User

article_ranking = Blueprint('article_ranking', __name__)


# 热度排行榜   作者：mc
@article_ranking.route("/article_ranking", methods=['POST'])
def ranking():
    data = request.get_json()
    action = data['action']
    value = []
    if action == '1':
        now = datetime.datetime.now()
        previous_time = now - datetime.timedelta(days=7)
        r_time = str(now).split(' ', 1)[0] + ' 00:00:00'
        l_time = str(previous_time).split(' ', 1)[0] + ' 00:00:00'
        result = Article.query.filter(and_(Article.send_time >= l_time, Article.send_time <= r_time)).order_by(
            desc('heat')).limit(100).all()
        for i in result:
            user = User.query.filter(User.id == i.user_id).first()
            value.append({
                'article_id': i.article_id,
                'title': i.title,
                'heat': i.heat

            })

    if action == '2':
        now = datetime.datetime.now()
        previous_time = now - datetime.timedelta(days=30)
        r_time = str(now).split(' ', 1)[0] + ' 00:00:00'
        l_time = str(previous_time).split(' ', 1)[0] + ' 00:00:00'
        result = Article.query.filter(and_(Article.send_time >= l_time, Article.send_time <= r_time)).order_by(
            desc('heat')).limit(100).all()
        for i in result:
            user = User.query.filter(User.id == i.user_id).first()
            value.append({
                'article_id': i.article_id,
                'title': i.title,
                'heat': i.heat
            })
    return jsonify(value)
