#!/usr/bin/python3
"""
User creation class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Define attributes for user
    """
    first_name = ""
    last_name = ""
    email = ""
    password = ""