from sqlalchemy import Column, Integer, String,DateTime

from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(50), unique=True)
    email = db.Column(String(120), unique=True)
    password = db.Column(String(120), unique=True)
    created_on = db.Column(DateTime)

    def __init__(self, **kwargs):
        # Helps with class initiation, basically what every attribute you give
        # at initiaion will become a class attribute with this __init__ method
        super(User, self).__init__(**kwargs)

    def to_full_json(self):
        json_user = {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'created_on': self.created_on
        }
        return json_user

    def __repr__(self):
        return '<User %r>' % (self.name)

    @staticmethod
    def from_json(json_post):
        name = json_post.get('name')
        email = json_post.get('email')
        password = json_post.get('password')
        created_on = json_post.get('created_on')

        user = User(
            name=name,
            email=email,
            password=password,
            created_on=created_on
        )
        return user