from flask import Blueprint, jsonify

from model.tag import Tag, db

get_tags = Blueprint('get_tags', __name__)


# get

@get_tags.route("/get_tags", methods=['GET', 'POST'])
def tag():
    tags_result = db.session.query(Tag).order_by(Tag.tag_heat.desc()).all()
    print(type(tags_result))
    arr = []
    for e in tags_result:
        arr.append({
            'tag_id': e.tag_id,
            'tag_name': e.tag_name
        })

    return jsonify(arr)
