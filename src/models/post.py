from sqlalchemy import Column, Integer, String,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    text = Column(String(500))
    created_on = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates = "posts")

    def __init__(self, text=None, created_on=None):
        self.text = text
        self.created_on = created_on
        

    def __repr__(self):
        return '<User %r>' % (self.name)