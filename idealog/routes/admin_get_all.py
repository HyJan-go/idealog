from flask import Blueprint

from model.admin import db

admin = Blueprint('admin', __name__)


# get


@admin.route('/create_db', methods=['GET'])
def create_db():
    db.create_all()
