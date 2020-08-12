from redis import StrictRedis
from sqlalchemy import distinct

from conf import redis_host, redis_port, redis_password
from model.admin import Admin
from model.article import Article, db
from model.category import Category
from model.comment import Comment
from model.reward import Reward
from model.tag import Tag
from model.user import User


# 判断用户是否存在
def exist_user(user_id):
    user = User.query.filter(User.id == user_id).first()
    if user is None:
        return False
    return True


# 判断管理员是否存在
def exist_admin(admin_id):
    admin = Admin.query.filter(Admin.admin_id == admin_id).first()
    if admin is None:
        return False
    return True


# 判断文章是否存在
def exist_article(article_id):
    article = Article.query.filter(Article.article_id == article_id).first()
    if article is None:
        return False
    return True


# 判断标签是否存在
def exist_tag(tag_id):
    tag = Tag.query.filter(Tag.tag_id == tag_id).first()
    if tag is None:
        return False
    return True


# 判断分类是否存在
def exist_category(category_id):
    category = Category.query.filter(Category.category_id == category_id).first()
    if category is None:
        return False
    return True


# 判断评论是否存在
def exist_comment(comment_id):
    comment = Comment.query.filter(Comment.comment_id == comment_id).first()
    if comment is None:
        return False
    return True


# 根据cookie返回用户id
def     get_user_id_by_cookie(request):
    uid = request.cookies.get('token')
    redis = get_redis_cli()
    result = redis.get("user:" + str(uid))
    if result is None:
        return None
    user = eval(result.decode("utf-8"))
    return user['id']


# 获取redis客户端
def get_redis_cli():
    redis = StrictRedis(host=redis_host, port=redis_port, password=redis_password)
    return redis


# 根据cookie获取用户信息(字典类型)
def get_user_dict_by_cookie(request):
    uid = request.cookies.get('token')
    redis = get_redis_cli()
    result = redis.get("user:" + str(uid))
    user = eval(result.decode("utf-8"))
    return user


# 根据cookie获取管理员id
def get_admin_id_by_cookie(request):
    uid = request.cookies.get('admin_token')
    redis = get_redis_cli()
    result = redis.get("admin:" + str(uid))
    admin = eval(result.decode("utf-8"))
    return admin['admin_id']


# 根据cookie获取管理员信息(字典类型)
def get_admin_dict_by_cookie(request):
    uid = request.cookies.get('admin_token')
    redis = get_redis_cli()
    result = redis.get("admin:" + str(uid))
    admin = eval(result.decode("utf-8"))
    return admin


# 获取用户的点赞数
def get_user_fabulous_num(user_id):
    # 先获取用户所发的所有的文章
    articles = Article.query.filter(Article.user_id == user_id).all()
    sum = 0
    for article in articles:
        sum += int(article.fabulous_num)
    return sum


# 获取用户的被打赏数,由于用户可能多次打赏，所以应该去重,获取打赏人数
def get_user_reward_num(user_id):
    num = db.session.query(distinct(Reward.user_id)).filter(Reward.be_reward_user_id == user_id).all()
    return len(num)


# 判断用户是否还在登录状态
def is_user_login(request):
    uid = request.cookies.get('token')
    redis = get_redis_cli()
    result = redis.get("user:" + str(uid))
    if result is None:
        return False
    return True


# 判断管理员是不是已经登录
def is_admin_login(request):
    uid = request.cookies.get('admin_token')
    redis = get_redis_cli()
    result = redis.get("admin:" + str(uid))
    if result is None:
        return False
    return True
