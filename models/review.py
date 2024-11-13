#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel"""
    place_id = ""  # Place .id reference
    user_id = ""  # User.id reference
    text = ""
