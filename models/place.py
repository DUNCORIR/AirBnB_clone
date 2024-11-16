#!/usr/bin/python3

from models.base_model import BaseModel


class Place(BaseModel):
    """Place class that inherits from BaseModel"""
    city_id = ""  # City.id reference
    user_id = ""  # user.id reference
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # List of amenity.id references
