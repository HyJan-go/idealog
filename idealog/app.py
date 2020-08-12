import time

from flask import request

from flask_apscheduler import APScheduler
from common.commons import get_user_id_by_cookie

from conf import app
from model.reward import Reward
from model.user import User, db


def route_register():
    from backstage.route_api import test, db
    from routes.deliver import deliver
    from routes.notice_remind import notice_remind
    from routes.admin_get_all import admin
    from routes.admin_login import login
    from routes.title_find import find
    from routes.user_login import user
    from routes.article_detail import article_detail
    from routes.user_set import setUser
    from routes.user_list_slice import user_list
    from routes.user_search_with_id import user_list_id
    from routes.user_update_pwd import ud_pwd
    from routes.follow import follow
    from routes.upload import upload
    from routes.get_tags import get_tags
    from routes.admin_del_user import del_user
    from routes.admin_active_user import active_user
    from routes.article_list import article_list
    from routes.user_like import like_article
    from routes.user_del_article import del_article
    from routes.follow__list import follow_list
    from routes.comment import comment
    from routes.user_update_information import update_information
    from routes.get_fans import fans_list
    from routes.ad_update_pwd import ad_ud_pwd
    from routes.user_profile import get_user_profile
    from routes.update_article import update_article
    from routes.article_collection import article_collection
    from routes.get_category import category
    from routes.notice_list import notice_list
    from routes.user_reward import reward
    from routes.article_ranking import article_ranking
    from routes.reward_list import reward_list
    from routes.quit import quit
    app.register_blueprint(admin)
    app.register_blueprint(user_list)
    app.register_blueprint(user_list_id)
    app.register_blueprint(test)
    app.register_blueprint(user)
    app.register_blueprint(setUser)
    app.register_blueprint(login)
    app.register_blueprint(upload)
    app.register_blueprint(deliver)
    app.register_blueprint(article_detail)
    app.register_blueprint(find)
    app.register_blueprint(ud_pwd)
    app.register_blueprint(get_tags)
    app.register_blueprint(follow)
    app.register_blueprint(del_user)
    app.register_blueprint(active_user)
    app.register_blueprint(article_list)
    app.register_blueprint(like_article)
    app.register_blueprint(del_article)
    app.register_blueprint(follow_list)
    app.register_blueprint(comment)
    app.register_blueprint(fans_list)
    app.register_blueprint(update_information)
    app.register_blueprint(ad_ud_pwd)
    app.register_blueprint(get_user_profile)
    app.register_blueprint(update_article)
    app.register_blueprint(article_collection)
    app.register_blueprint(category)
    app.register_blueprint(notice_remind)
    app.register_blueprint(notice_list)
    app.register_blueprint(reward)
    app.register_blueprint(article_ranking)
    app.register_blueprint(reward_list)
    app.register_blueprint(quit)
    db.init_app(app)


class Config(object):  # 创建配置，用类     author:HyJan
    # 定时或循环任务列表
    JOBS = [
        {  # 创建一个定时任务，每天凌晨0点的时候，刷新数据库的状态，保证用户每天登陆都能收到5个虚拟金币
            'id': 'job',
            'func': '__main__:flush_status',  # 绑定方法名
            'trigger': 'cron',  # 任务类型： interval表示循环任务, cron表示定时任务
            'hour': 0
        }
    ]


# 全部用户的登录状态设置为未登录状态
def flush_status():
    users = db.session.query(User).all()
    # 设置为第一次的登录状态为1，获取的就是第一次登录了
    for user in users:
        user.first_login = 1
        db.session.commit()


app.config.from_object(Config())  # 为实例化的flask引入配置


# 全局拦截器，在请求之前做的事情，如果还是登录状态，就给他加金币
@app.before_request
def before_request():
    user_id = get_user_id_by_cookie(request)
    if user_id is not None:
        user = User.query.filter(User.id == user_id).first()
        # 如果今天还是首次登录，就加金币，改状态
        if user.first_login == 1:
            user.vir_money += 5
            user.first_login = 0
            # 添加记录
            reward_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # 如果打赏用户是0，article_id 也是0, 说明是系统打赏的
            reward = Reward(user_id, user_id, 5, reward_time, 0, "系统打赏")
            db.session.add(reward)
        db.session.commit()


if __name__ == '__main__':
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    route_register()
    app.run(debug=True, host='0.0.0.0')
