#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os

Base = declarative_base()


class DBStorage():
    """dbstorage engine"""
    __engine = None
    __session = None

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        database = os.getenv("HBNB_MYSQL_DB")
        env_test = os.getenv("HBNB_ENV")
        l_host = os.getenv("HBNB_MYSQL_HOST")
        storage_type = os.getenv("HBNB_TYPE_STORAGE")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:{}'.
                                      format(user, pwd, l_host, database),
                                      pool_pre_ping=True)

        if env_test == 'test':
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):

        self.__session = Session(self.__engine)
        query_dict = {}
        if cls is None:
            for clas in DBStorage.classes.values():
                objects = self.__session.query(clas).all()
                for object in objects:
                    key = object.__class__.__name__ + '.' + object.id
                    query_dict[key] = object
        else:
            if cls in DBStorage.classes.values():
                objects = self.__session.query(cls).all()
                for object in objects:
                    key = object.__class__.__name__ + '.' + object.id
                    query_dict[key] = object
        return query_dict

    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')
