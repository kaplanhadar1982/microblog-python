from sqlalchemy import Column, Integer, String,DateTime
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(120), unique=True)
    created_on = Column(DateTime)

    def __init__(self, name=None, email=None,password=None,created_on=None):
        self.name = name
        self.email = email
        self.password = password
        self.created_on = created_on

    def __repr__(self):
        return '<User %r>' % (self.name)