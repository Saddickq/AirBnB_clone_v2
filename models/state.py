#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""

    def __init__(self, *args, **kwargs):
            """Instantiates a new Place"""
            super().__init__(*args, **kwargs)

            # Handle unknown attributes
            for key, value in kwargs.items():
                if key not in dir(self):
                    setattr(self, key, value)