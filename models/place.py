#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
import os


class Place(BaseModel, Base):
    """ Class for Place Module """
    __tablename__ = "places"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Getter attribute that returns reviews whose
            id matches place_id"""
            from models import storage
            matched_results = []
            """get all the review objects i teh review file"""
            reviews = storage.all(Review)
            for review in reviews.values():
                """if review models place id matches the id of
                the current place id return those particular
                objects or instances"""
                if review.place_id == self.id:
                    matched_results.append(review)
            return matched_results
