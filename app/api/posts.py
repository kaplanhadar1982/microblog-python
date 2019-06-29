from flask import jsonify, request, current_app
from app.models.post import Post
from app.models.user import User
from app.api import api
from app import db
from app.utilities.jwt import decode_auth_token

@api.route('/posts', methods=['POST'])
def new_post():
    try:
        auth_token = request.json.get('token')
        user_id = decode_auth_token(auth_token)
        post = Post(text=request.json.get("text"),user_id=user_id,created_on=request.json.get("created_on"))
        current_app.logger.info('Creating new post')
        db.session.add(post)
        db.session.commit()
        return jsonify(post.to_full_json()), 201
    except Exception as e:
        current_app.logger.error('new_post' + str(e))
        return jsonify({"error": "something went worng"}), 500

@api.route('/posts', methods=['GET'])
def get_posts():
    try:
        auth_token = request.json.get('token')
        user_id = decode_auth_token(auth_token)
        user = db.session.query(User).get(user_id)
        return jsonify(user.to_full_json()), 200
    except Exception as e:
        current_app.logger.error('get_posts' + str(e))
        return jsonify({"error": "something went worng"}), 500