#!/usr/bin/python3
"""
Module creates a User Class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Define attributes for user
    """
    first_name = ""
    last_name = ""
    email = ""
    password = ""
