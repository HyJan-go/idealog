from flask import request, jsonify, Blueprint
from sqlalchemy import distinct

from common.commons import exist_article, exist_user, get_user_id_by_cookie
from model.article import Article, db
from model.collection import Collection
from model.fabulous import Fabulous
from model.follow import Follow
from model.reward import Reward
from model.user import User

article_detail = Blueprint('article_detail', __name__)


# get

# 根据前端获得的文档id和当前登录用户的id,先通过Redis进行查询，查询不到就要到数据库查，返回相应的字段 author:HyJan
@article_detail.route('/art/dtl', methods=['GET', 'POST'])
def get_article_detail():
    data = request.get_json()
    article_id = data['article_id']
    user_id = get_user_id_by_cookie(request)
    print(user_id)
    if exist_article(article_id):
        detail = get_detail_from_db(article_id)
        detail.heat = int(detail.heat) + int(1)
        detail.look_num = int(detail.look_num) + 1
        db.session.commit()
        tag_id = detail.tag_id
        tag_id = str(tag_id)
        ids = tag_id.split(",")
        tag_ids = json_for_tag_id(ids)
        name = detail.tag_name
        names = name.split(",")
        tag_names = json_for_tag_name(names)

        # 如果用户是没有登录的状态
        if user_id is None:
            article_detail = serial(detail, 0, tag_ids, tag_names, 0, is_collection(-1, article_id),
                                    get_user(detail.user_id), get_reward_number(article_id))
            return jsonify(article_detail)
        # 如果是登录状态
        else:
            if exist_user(user_id):
                concern = Follow.query.filter(Follow.user_id == user_id,
                                              Follow.followed_id == detail.user_id).first()
                like = Fabulous.query.filter(Fabulous.user_id == user_id, Fabulous.article_id == article_id).first()
                if concern is None and (like is None or like.fabulous_status == 0):
                    article_detail = serial(detail, 0, tag_ids, tag_names, 0,
                                            is_collection(user_id, article_id),
                                            get_user(detail.user_id), get_reward_number(article_id))
                    return jsonify(article_detail)
                elif concern is not None and (like is None or like.fabulous_status == 0):
                    article_detail = serial(detail, 1, tag_ids, tag_names, 0,
                                            is_collection(user_id, article_id),
                                            get_user(detail.user_id), get_reward_number(article_id)
                                            )
                    return jsonify(article_detail)
                elif concern is None and like.fabulous_status != 0:
                    article_detail = serial(detail, 0, tag_ids, tag_names, 1,
                                            is_collection(user_id, article_id),
                                            get_user(detail.user_id), get_reward_number(article_id)
                                            )
                    return jsonify(article_detail)
                else:
                    article_detail = serial(detail, 1, tag_ids, tag_names, 1,
                                            is_collection(user_id, article_id),
                                            get_user(detail.user_id), get_reward_number(article_id)
                                            )
                    return jsonify(article_detail)
            # 用户不存在和未登录的返回应该是一样的
            else:
                article_detail = serial(detail, 0, tag_ids, tag_names, 0, is_collection(user_id, article_id),
                                        get_user(detail.user_id), get_reward_number(article_id))
                return jsonify(article_detail)
    else:
        return jsonify({"code": "203", "msg": "抱歉，文章不存在"})


def get_detail_from_db(article_id):
    detail = db.session.query(Article).get(article_id)
    return detail


# 数据库中取出来的list进行json化方式
def serial(detail, status, tag_ids, tag_names, like_status, collection_status, user, reward_number):
    article_detail = {
        'user_id': detail.user_id,
        'user_name': user.nick_name,
        'title': detail.title,
        'effect': user.effect,
        'reward_status': detail.reward_status,
        'content': detail.content,
        'send_time': str(detail.send_time),
        'fabulous_num': detail.fabulous_num,
        'comment_num': detail.comment_num,
        'category_id': detail.category_id,
        'category_name': detail.category_name,
        'status': str(status),
        'tag_ids': tag_ids,
        'tag_names': tag_names,
        'like_status': like_status,
        'collection_status': collection_status,
        'head_pic': str(user.avatar),
        'look_num': str(detail.look_num),
        'reward_addr': str(user.reward_addr),
        'reward_number': reward_number
    }
    return article_detail


# 格式化tag_id
def json_for_tag_id(ids):
    detail = []
    for i in ids:
        print(type(i))
        detail.append({
            "tag_id" + str(ids.index(i) + 1): str(i)
        })
    return detail


# 格式化tag_name
def json_for_tag_name(names):
    detail = []
    for i in names:
        print(type(i))
        detail.append({
            "tag_name" + str(names.index(i) + 1): str(i)
        })
    return detail


# 用户对文章的收藏状态，如果是1，则是收藏状态，如果是0，则不是收藏状态
def is_collection(user_id, article_id):
    collection = Collection.query.filter(Collection.user_id == user_id, Collection.article_id == article_id).first()
    if collection is None:
        return 0
    return 1


# 获取文章作者头像
def get_user(user_id):
    user = User.query.filter(User.id == user_id).first()
    return user


# 获取文章的打赏人数
def get_reward_number(article_id):
    result = db.session.query(distinct(Reward.user_id)).filter(Reward.article_id == article_id).all()
    return len(result)
