#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
<<<<<<< HEAD
import os

=======
from models import storage_type
>>>>>>> cf9ab4e566992767b58b2ccaf7f081b936de7604

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
<<<<<<< HEAD
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
=======
    if storage_type == "db"
>>>>>>> cf9ab4e566992767b58b2ccaf7f081b936de7604
        name = Column(String(128),
                      nullable=False)
    else:
        name = ""
