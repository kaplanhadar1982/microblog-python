from flask import jsonify, request, current_app

from app import db
from app.api import api
from app.models.post import Post
from app.models.user import User
from app.models.vote import Vote
from app.utilities.jwt import decode_auth_token


@api.route('/votes/upvote', methods=['POST'])
def upvote():

    try:
        current_app.logger.info('upvote')
        auth_token = request.json.get('token')
        user_id = decode_auth_token(auth_token)
        post = db.session.query(Post).get(request.json.get('post_id'))
        if (post.user_id == user_id):
            return jsonify({"error": "user cant upvote his post"}), 500
        existing_vote = db.session.query(Vote).filter_by(user_id=user_id,post_id=post.id).first()
        if(existing_vote != None):
            return jsonify({"error": "user cant upvote more than onces for his post"}), 500
        vote = Vote(user_id=user_id,post_id=request.json.get('post_id'),created_on=request.json.get("created_on"))
        db.session.add(vote)
        db.session.commit()
        return jsonify(vote.to_full_json()), 201
    except Exception as e:
        current_app.logger.error('upvote' + str(e))
        return jsonify({"error": "something went worng"}), 500



@api.route('/votes/downvote', methods=['POST'])
def downvote():

    try:
        current_app.logger.info('downvote')
        auth_token = request.json.get('token')
        user_id = decode_auth_token(auth_token)
        existing_vote = db.session.query(Vote).filter_by(user_id=user_id,post_id=request.json.get('post_id')).first()
        if(existing_vote == None):
            return jsonify({"error": "not such post"}), 500
        db.session.delete(existing_vote)
        db.session.commit()
        return jsonify({"message": "downvote the post"}), 200
    except Exception as e:
        current_app.logger.error('downvote' + str(e))
        return jsonify({"error": "something went worng"}), 500