#!/usr/bin/python3
"""
review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Reviews made by users
    """
    text = ""
    place_id = ""
    user_id = ""
