#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv
from sqlalchemy.orm import relationship


class DBStorage():
    """dbstorage engine"""
    __engine = None
    __session = None

    classes = {
        'User': User, 'Place': Place, 'State': State,
        'City': City, 'Review': Review
    }

    def __init__(self):
        """database storage"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        database = getenv("HBNB_MYSQL_DB")
        env_test = getenv("HBNB_ENV")
        host = getenv("HBNB_MYSQL_HOST")
        storage_type = getenv("HBNB_TYPE_STORAGE")

        try:
            self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                          format(user, pwd, host, database),
                                          pool_pre_ping=True)
        except Exception as error:
            print(error)

        if env_test == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query database for all types of objects"""
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        query_dict = {}
        if cls is None:
            for clas in DBStorage.classes.values():
                objects = self.__session.query(clas).all()
                for objc in objects:
                    key = "{}.{}".format(objc.__class__.__name__, objc.id)
                    query_dict[key] = objc
        else:
            if cls in DBStorage.classes.values():
                objects = self.__session.query(cls).all()
                for objc in objects:
                    key = "{}.{}".format(objc.__class__.__name__, objc.id)
                    query_dict[key] = objc
        return query_dict

    def new(self, obj):
        """ add the object to the current database session """
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session"""
        if obj:
            cls = type(obj)
            self.__session.query(cls).filter(cls.id == obj.id).delete()

    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """close a session"""
        self.__session.close()
