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
            del kwargs['__class__']
            kwargs['created_at'] = datetime.fromisoformat(
                    kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(
                    kwargs['updated_at'])
            self.__dict__.update(kwargs)
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
