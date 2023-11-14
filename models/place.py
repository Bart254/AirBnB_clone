#!/usr/bin/python3
"""
Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defines Place class
    """
    name = ""
    description = ""
    city_id = ""
    user_id = ""
    number_bathrooms = 0
    number_rooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
