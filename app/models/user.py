from flask import jsonify
from datetime import datetime,timedelta
from app import db,bcrypt
from decouple import config
from app.utilities.jwt import encode_auth_token


from app.models.post import Post

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    posts = db.relationship("Post", order_by = Post.id, back_populates = "user")

    def __init__(self, **kwargs):
        # Helps with class initiation, basically what every attribute you give
        # at initiaion will become a class attribute with this __init__ method
        super(User, self).__init__(**kwargs)

    def to_full_json(self):
        json_user = {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'token': str(encode_auth_token(self.id)),
            'created_on': self.created_on,
            'posts': str([p for p in self.posts])
        }
        return json_user

    def __repr__(self):
        return '<User %r>' % (self.name)

    @staticmethod
    def from_json(json_post):
        name = json_post.get('name')
        email = json_post.get('email')
        password = bcrypt.generate_password_hash(
            json_post.get('password'), config("BCRYPT_LOG_ROUNDS", cast=int, default=8) 
        ).decode()
        created_on = json_post.get('created_on')

        user = User(
            name=name,
            email=email,
            password=password,
            created_on=created_on
        )
        return user


    

    
