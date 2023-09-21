from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review
from models.amenity import Amenity


class Place(BaseModel, Base):
    """ Class for Place Module """
    __tablename__ = "places"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
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

        place_amenity = Table(
            'place_amenity',
            Base.metadata,
            Column('place_id', String(60), ForeignKey(
                'places.id'), primary_key=True, nullable=False),
            Column('amenity_id', String(60), ForeignKey(
                'amenities.id'), primary_key=True, nullable=False),
            PrimaryKeyConstraint('place_id', 'amenity_id')
        )

        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False
        )

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
            """get all the review objects in the review file"""
            reviews = storage.all(Review)
            for review in reviews.values():
                """if review model's place id matches the id of
                the current place id return those particular
                objects or instances"""
                if review.place_id == self.id:
                    matched_results.append(review)
            return matched_results
        amenity_ids = []

        @property
        def amenities(self):
            """
            Getter attribute that returns a list of Amenity instances
            based on the attribute amenity_ids that contains all Amenity.id
            linked to the Place.
            """
            from models import storage
            amenity_instances = []
            for amenity_id in self.amenity_ids:
                amenity = storage.get(Amenity, amenity_id)
                if amenity:
                    amenity_instances.append(amenity)
            return amenity_instances

        @amenities.setter
        def amenities(self, obj):
            """
            Setter attribute that handles the append method for adding an
            Amenity.id to the attribute amenity_ids. This method should
            accept only Amenity object, otherwise, do nothing.
            """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
