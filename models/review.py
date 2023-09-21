#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import storage_type


class Review(BaseModel, Base):
    """Review class"""
    __tablename__ = 'reviews'

    if storage_type == "db":
        text = Column(String(1024),
                      nullable=False)
        place_id = Column(String(60),
                          ForeignKey('places.id'),
                          nullable=False)
        user_id = Column(String(60),
                         ForeignKey('users.id'),
                         nullable=False)
    else:
        text = ""
        place_id = ""
        user_id = ""
