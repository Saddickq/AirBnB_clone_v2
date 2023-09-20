#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel():
    """A base class for all hbnb models"""
    id = Column(String(60),
                nullable=False,
                primary_key=True)
    created_at = Column(DateTime,
                        nullable=False,
                        default=datetime.utcnow())
    updated_at = Column(DateTime,
                        nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        from models import storage

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if not hasattr(self, key):
                    setattr(self, key, value)

            fmt = '%Y-%m-%dT%H:%M:%S.%f'
            if kwargs.get('updated_at') or kwargs.get('created_at'):
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                         fmt)
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                         fmt)

            if kwargs.get('__class__'):
                del kwargs["__class__"]
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        for key in dictionary.keys():
            if type(dictionary[key]) is datetime:
                dictionary[key] = dictionary[key].isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """used to delete the current instance from the Filestorage"""
        from models import storage
        storage.delete(self)
