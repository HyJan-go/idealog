import datetime
import time
from datetime import timedelta

from flask import request, jsonify, Blueprint
from sqlalchemy import and_, func

from model.article import Article
from model.collection import Collection
from model.user import User, db

article_list = Blueprint('article_list', __name__)

article_list_conf = {'page_index': 1, 'page_size': 15}


# get

# author: wuchuming
# 获取文章列表
# 从数据库中根据条件获取所需文章并返回
@article_list.route('/art/list', methods=['POST'])
def get_article_list():
    data = request.get_json()
    # 当需要增加筛选条件时，在此处添加参数
    item_dict = {
        'filter': {'user_id': None, 'tag_id': None, 'this_week': None, 'this_month': None, 'title': None,
                   'category_id': None},
        'sort': {'seq': None, 'hot': None}
    }
    for pkey, pvalue in item_dict.items():
        for key in pvalue.keys():
            if (key in data):
                item_dict[pkey][key] = data.get(key)
    set_page(data)
    return select_items(**item_dict)


# author: wuchuming
# 根据item_dict中对应参数值进行过滤及排序
def select_items(**item_dict):
    query = db.session.query(Article)
    filter_item = item_dict['filter']
    for p_item, p_value in item_dict.items():
        for item, value in p_value.items():
            if value is not None and (value != ""):
                query = function_dict[item](query, value)
    articles = query.order_by(Article.send_time.desc()).order_by(Article.article_id).offset(
        (article_list_conf['page_index'] - 1) * article_list_conf['page_size']).limit(
        article_list_conf['page_size']).all()
    return json_format(articles)


# author: wuchuming
# 设置页号及页大小
def set_page(data):
    # 取页号，安卓端默认[page_index=1,page_size=5*15]，网页默认page_size=15
    if ('page_index' in data and (data.get('page_index') != "")):
        article_list_conf['page_index'] = int(data.get('page_index'))
        article_list_conf['page_size'] = 15
    else:
        article_list_conf['page_index'] = 1
        article_list_conf['page_size'] = 15 * 5


# author: wuchuming
# 根据用户id查询获取其文章列表
def select_by_uid(query, str_user_id):
    try:
        user_id = int(str_user_id)
    except ValueError as ve:
        print('error : invalid user_id')
    else:
        return query.filter(Article.user_id == user_id)
    return query


# author: wuchuming
# 根据标签过滤文章列表
# 计算传入标签所有子集，再逐个计算子集的全排列，得到所有可能的组合
def select_by_tags(query, str_tag_ids):
    tag_ids = str_tag_ids.split(',')
    permutation_sub_tags = get_permutation(compute_sub_tags(tag_ids))
    for i in range(len(permutation_sub_tags)):
        permutation_sub_tags[i] = ','.join(permutation_sub_tags[i])
    # rule = or_(*[Article.tag_id.like(tid) for tid in tag_ids])
    return query.filter(Article.tag_id.in_(permutation_sub_tags))


# author: wuchuming
# 计算tag_ids的子集
def compute_sub_tags(tag_ids):
    sub_tags = [[]]
    for tag_id in tag_ids:
        sub_length = len(sub_tags)
        for i in range(sub_length):
            s_tag = list(sub_tags[i])
            s_tag.append(tag_id)
            sub_tags.append(s_tag)
    return sub_tags


# author: wuchuming
# 计算每个非空子集的全排列
# FIXME: 使用多路归并实现
def get_permutation(sub_tags):
    permut_sub_tags = []
    for s_tag in sub_tags:
        if len(s_tag) <= 0:
            continue
        permut_sub_tags.extend(compute_permutation(s_tag))
    return permut_sub_tags


def compute_permutation(s_tag):
    result = [[]]
    result[0].append(s_tag[0])
    if len(s_tag) <= 1:
        return result
    for i in range(1, len(s_tag)):
        tmp_res = []
        for res in result:
            tmp = list(res)
            tmp.insert(0, s_tag[i])
            tmp_res.append(tmp)
            tmp = list(res)
            tmp.append(s_tag[i])
            tmp_res.append(tmp)
            for j in range(1, len(res)):
                tmp = list(res)
                tmp.insert(j, s_tag[i])
                tmp_res.append(tmp)
        result = tmp_res
    return result


# author: wuchuming
# 筛选本周内的文章列表
def select_by_this_week(query, this_week):
    if this_week == '1':
        now = datetime.datetime.now()
        this_week_start = now - timedelta(days=now.weekday())
        l_time = str(this_week_start).split(' ', 1)[0] + ' 00:00:00'
        r_time = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        return query.filter(and_(Article.send_time >= l_time, Article.send_time <= r_time))
    return query


# author: wuchuming
# 筛选本月内的文章列表
def select_by_this_month(query, this_month):
    if this_month == '1':
        now = datetime.datetime.now()
        this_month_start = datetime.datetime(now.year, now.month, 1)
        l_time = str(this_month_start)
        r_time = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        return query.filter(and_(Article.send_time >= l_time, Article.send_time <= r_time))
    return query


# 根据文章标题筛选文章列表
def select_by_title(query, title):
    return query.filter(Article.title.like("%" + title + "%"))


# author: wuchuming
# 根据分类筛选文章列表
def select_by_category(query, str_category_id):
    try:
        category_id = int(str_category_id)
    except ValueError as ve:
        return query
    else:
        return query.filter(Article.category_id == category_id)


# author: wuchuming
# 根据点赞数获取文章列表
def sort_by_fabulous(query, hot):
    if hot == '1':
        return query.order_by(Article.fabulous_num.desc())
    else:
        return query.order_by(Article.fabulous_num)


# author: wuchuming
# 根据发表时间获取文章列表
def sort_by_send_time(query, seq):
    if seq == '1':
        return query.order_by(Article.send_time.desc())
    else:
        return query.order_by(Article.send_time)


# 当需要增加筛选条件时，在此注册函数
function_dict = {
    'user_id': select_by_uid,
    'tag_id': select_by_tags,
    'seq': sort_by_send_time,
    'hot': sort_by_fabulous,
    'this_week': select_by_this_week,
    'this_month': select_by_this_month,
    'title': select_by_title,
    'category_id': select_by_category
}


# author: wuchuming
# 根据文章id从article表中获取文章详情
def from_db_select(article_ids):
    for i in range(len(article_ids)):
        article_ids[i] = str(article_ids[i]).split('(', 1)[1].split(',', 1)[0]
    articles = db.session.query(Article).filter(Article.article_id.in_(article_ids)).all()
    return json_format(articles, article_ids)


# author: wuchuming
# 将数据库中过滤出来的记录格式化
# 可根据article_ids指定顺序
# articles中记录数应与articles_ids长度严格一致
def json_format(articles, v_article_ids=[]):
    if len(v_article_ids) > 0:
        dict_article = {}
        for article in articles:
            dict_article.update({str(article.article_id): article})
        j = 0
        for i in range(len(v_article_ids)):
            if v_article_ids[i] in dict_article.keys():
                articles[j] = dict_article[v_article_ids[i]]
                j += 1
    value = []
    for article in articles:
        user = User.query.filter(User.id == article.user_id).first()
        value.append({
            'article_id': article.article_id,
            'user_id': article.user_id,
            'user_name': user.nick_name,
            'title': article.title,
            'content': article.content,
            'enclosure_addr': article.enclosure_addr,
            'content_pic': article.content_pic,
            'send_time': str(article.send_time),
            'update_time': str(article.update_time),
            'tag_id': article.tag_id,
            'category_id': article.category_id,
            'tag_name': article.tag_name,
            'category_name': article.category_name,
            'fabulous_num': article.fabulous_num,
            'comment_num': article.comment_num,
            'look_num': article.look_num,
            'author_pic': user.avatar
        })
    return jsonify(value)


# author: wuchuming
# 获取某用户收藏文章列表
@article_list.route('/art/list/collection', methods=['POST'])
def get_collection_list():
    data = request.get_json()
    set_page(data)
    uid = data.get('user_id')
    return select_collection_article(uid)


# author: wuchuming
# 根据用户id查询其收藏文章 
def select_collection_article(uid):
    query = db.session.query(Collection.article_id).filter(Collection.user_id == uid).order_by(
        Collection.collection_time.desc())
    article_ids = query.order_by(Collection.collection_id).offset(
        (article_list_conf['page_index'] - 1) * article_list_conf['page_size']).limit(
        article_list_conf['page_size']).all()
    return from_db_select(article_ids)


# author: wuchuming
# 获取文章总页数
@article_list.route('/art/list/get_all_page', methods=['POST', 'GET'])
def get_all_page():
    data = request.get_json()
    page_dict = {
        'LIST_OF_ARTICLE': lambda anything: db.session.query(func.count(Article.article_id)).scalar(),
        'LIST_OF_COLLECTION': lambda user_id: db.session.query(func.count(Collection.collection_id)) \
            .join(Article, Collection.article_id == Article.article_id) \
            .filter(Collection.user_id == user_id).scalar(),
    }
    all_counts = 0
    try:
        key = data.get('method_of_slice')
        all_counts = page_dict[key](int(data.get('user_id')) if ('user_id' in data.keys()) else None)
    except Exception as e:
        repr(e)
        return jsonify({'code': 203, 'all_page': 0, 'msg': 'invaild request args or db exception'})
    # print("++++++++++++++"+str(all_counts))
    all_page = 0
    while (all_counts > 0):
        all_page += 1
        all_counts -= 15
    return jsonify({'code': 200, 'all_page': all_page})
