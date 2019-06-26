# from sqlalchemy import Column, Integer, String,DateTime,ForeignKey
# from sqlalchemy.orm import relationship
# from database import Base

# class Post(Base):
#     __tablename__ = 'posts'
#     id = Column(Integer, primary_key=True)
#     text = Column(String(500))
#     created_on = Column(DateTime)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     user = relationship("User", back_populates = "posts")

#     def __init__(self, text=None, created_on=None):
#         self.text = text
#         self.created_on = created_on
        

#     def __repr__(self):
#         return '<User %r>' % (self.name)

from datetime import datetime
from app import db

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500))
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates = "posts")

    def __init__(self, **kwargs):
        # Helps with class initiation, basically what every attribute you give
        # at initiaion will become a class attribute with this __init__ method
        super(Post, self).__init__(**kwargs)

    def to_full_json(self):
        json_post = {
            'id': self.id,
            'text': self.text,
            'user_id': self.user_id,
            'created_on': self.created_on
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