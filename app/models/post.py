from datetime import datetime
from app import db
from app.models.vote import Vote


class Post(db.Model):

    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500))
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates = "posts")
    votes = db.relationship("Vote", order_by = Vote.user_id, back_populates = "post")

    def __init__(self, **kwargs):
        # Helps with class initiation, basically what every attribute you give
        # at initiaion will become a class attribute with this __init__ method

        super(Post, self).__init__(**kwargs)


    def to_full_json(self):

        json_post = {
            'id': self.id,
            'text': self.text,
            'user_id': self.user_id,
            'created_on': self.created_on,
            'votes': len(self.votes)
        }
        return json_post


    def __repr__(self):

        return '<Post %r>' % (self.text)


    @staticmethod
    def from_json(json_post):

        text = json_post.get('text')
        user_id = json_post.get('user_id')

        post = Post(
            text=text,
            user_id=user_id
        )
        return post