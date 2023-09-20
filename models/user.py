#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(BaseModel):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    places = relationship('Place', 
                          backref='user',
                          cascade='all, delete-orphan')
    reviews = relationship('Review', 
                           backref='user', 
                           cascade='all, delete-orphan')