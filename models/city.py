#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
<<<<<<< HEAD
import os
=======
from models import storage_type
>>>>>>> cf9ab4e566992767b58b2ccaf7f081b936de7604


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
<<<<<<< HEAD
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
=======
    if storage_type == 'db':
>>>>>>> cf9ab4e566992767b58b2ccaf7f081b936de7604
        name = Column(String(128), nullable=False)
        state_id = Column(String(60),
                          ForeignKey('states.id'),
                          nullable=False)
        places = relationship('Place',
                              backref='cities',
                              cascade='all, delete-orphan')
    else:
        name = ""
        state_id = ""
