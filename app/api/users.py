from flask import jsonify, request, current_app
from app.models.user import User
from app.api import api
from app import db,bcrypt


@api.route('/users', methods=['POST'])
def new_user():

    try:
        user = User.from_json(request.json)
        current_app.logger.info('Creating new user')
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_full_json()), 201
    except Exception as e:
        current_app.logger.error('Creating new user' + str(e))
        return jsonify({"error": "something went worng"}), 500


@api.route('/users', methods=['GET'])
def get_all_users():

    current_app.logger.info('Get all users')
    return jsonify([u.to_full_json() for u in db.session.query(User).all()]), 200


@api.route('/users/login', methods=['POST'])
def login():

    try:
        current_app.logger.info('login')
        json_email = request.json.get('email')
        json_password = request.json.get('password')
        user = User.query.filter_by(email=json_email).first()
        if user != None and bcrypt.check_password_hash(user.password, json_password):
            return jsonify(user.to_full_json()), 200
        return jsonify({"error": "unautherized"}),401
    except Exception as e:
        current_app.logger.error('Creating new user' + str(e))
        return jsonify({"error": "something went worng"}), 500

    