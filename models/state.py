#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128),
                      nullable=False)
    else:
        name = ""

        @property
        def cities(self):
            """ Returns a list of city objects """
            from models import storage
            cities = storage.all(City).values()
            return list(filter(lambda city: city.state_id == self.id, cities))
