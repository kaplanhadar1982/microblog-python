from flask import jsonify, request, current_app
from app.models.post import Post
from app.models.user import User
from app.api import api
from app import db

@api.route('/posts', methods=['POST'])
def new_post():
    post = Post.from_json(request.json)
    current_app.logger.info('Creating new post')
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_full_json()), 201

@api.route('/posts', methods=['GET'])
def get_posts():
    user = db.session.query(User).get(1)
    return jsonify(user.to_full_json()), 200