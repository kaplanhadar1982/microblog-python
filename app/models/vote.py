from app import db
from datetime import datetime


class Vote(db.Model):

    __tablename__ = 'votes'
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    post = db.relationship("Post")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    user = db.relationship("User")
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)


    def __init__(self, **kwargs):
        # Helps with class initiation, basically what every attribute you give
        # at initiaion will become a class attribute with this __init__ method

        super(Vote, self).__init__(**kwargs)


    def to_full_json(self):

        json_post = {
            'post_id': self.post_id,
            'user_id': self.user_id,
            'created_on': self.created_on
        }
        return json_post

