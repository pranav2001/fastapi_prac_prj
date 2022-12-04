from ast import Str
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from email.policy import default
from http import server
from turtle import title
from .database import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean,ForeignKey

class Post(Base):
    __tablename__="posts"

    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content= Column(String,nullable=False)
    published= Column(Boolean, server_default='TRUE',nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)

    owner=relationship("User")

class User(Base):
    __tablename__='users'

    id = Column(Integer,primary_key=True,nullable=False)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    phone_number=Column(String)
class Vote(Base):
    __tablename__="votes"
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
    