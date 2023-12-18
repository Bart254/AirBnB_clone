#!/usr/bin/python3
""" Module creates a BaseModel class
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ BaseModel Class
    """
    def __init__(self, *args, **kwargs):
        """ defines common attributes of objects
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                self.__dict__.update({key: value})
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """returns class name, id, attribute dictionary
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """ updates time
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ Returns dictionary representation of object
        """
        new_dict = {}
        for i, j in self.__dict__.items():
            if i == "created_at" or i == "updated_at":
                new_dict[i] = j.isoformat()
            else:
                new_dict[i] = j
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
