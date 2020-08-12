from flask import jsonify, Blueprint

from model.category import Category

# author:陈樱脡  获取分类列表
category = Blueprint('category', __name__)


# get

@category.route('/getClass', methods=['GET', 'POST'])
def get_category():
    category = Category.query.all()
    list = []
    for i in category:
        list.append({
            'category_id': i.category_id,
            'cate_name': i.cate_name
        })
    return jsonify(list)
