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
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj.to_dict()

    def save(self):
        """ Serializes dictionary to the JSON file
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """ Deserializes JSON file
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                self.__objects = json.load(f)
        except (FileNotFoundError):
            pass
