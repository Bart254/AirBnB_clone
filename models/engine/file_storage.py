#!/usr/bin/python3
""" File Storage Module
"""
import json


class FileStorage:
    """ File Storage Class
    file_path(priv attribute): stores the path to json file
    objects(priv): a dictionary containing python objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary of objects
        """
        return self.__objects

    def new(self, obj):
        """ sets in dictionary with obj and <obj class name>.id as key
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Serializes dictionary to the JSON file
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            temp = {}
            for key, obj in self.__objects.items():
                temp.update({key: obj.to_dict()})
            json.dump(temp, f)

    def reload(self):
        """ Deserializes JSON file
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'City': City, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                temp = json.load(f)
                for key, obj_dict in temp.items():
                    obj = classes[obj_dict['__class__']](**obj_dict)
                    self.__objects[key] = obj
        except (FileNotFoundError):
            pass
