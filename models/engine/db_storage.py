#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
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
        """database storage"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        database = getenv("HBNB_MYSQL_DB")
        env_test = getenv("HBNB_ENV")
        host = getenv("HBNB_MYSQL_HOST")
        storage_type = getenv("HBNB_TYPE_STORAGE")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, database),
                                      pool_pre_ping=True)

        if env_test == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query database for all types of objects"""
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        query_dict = {}
        try:
            if cls is None:
                for clas in DBStorage.classes.values():
                    objects = self.__session.query(clas).all()
                    for object in objects:
                        key = "{}.{}".format(object.__class__.__name__, object.id)
                        query_dict[key] = object
            else:
                if cls in DBStorage.classes.values():
                    objects = self.__session.query(cls).all()
                    for object in objects:
                        key = "{}.{}".format(object.__class__.__name__, object.id)
                        query_dict[key] = object
            return query_dict
        except Exception as error:
            print(f"An ERROR occurred: {error}")
            self.__session.rollback()
        finally:
            self.__session.close()

    def new(self, obj):
        """ add the object to the current database session """
        self.__session = Session()
        try:
            new_obj = obj.__class__.__name__(obj)
            self.__session.add(new_obj)
        except Exception as error:
            print(f"An ERROR occurred: {error}")
            self.__session.rollback()
        finally:
            self.__session.close()

    def save(self):
        """ commit all changes of the current database session """
        self.__session = Session()
        try:
            self.__session.commit()
        except Exception:
            pass
        finally:
            self.__session.close()

    def delete(self, obj=None):
        """ delete from the current database session"""
        self.__session = Session()
        if obj:
            try:
                cls = type(obj)
                self.__session.query(cls).filter(cls.id == obj.id).delete()
            except Exception as error:
                self.__session.rollback()
                print(f"An ERROR occured: {error}")
            finally:
                self.__session.close()
    
    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
