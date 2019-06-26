from flask import jsonify, request, current_app
from app.models.user import User
from app.api import api
from app import db

@api.route('/users')
def users():
    return 'users'


@api.route('/users/', methods=['POST'])
def new_user():
    # Used for creating a new story
    user = User.from_json(request.json)
    current_app.logger.info('Creating new user')
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_full_json()), 201