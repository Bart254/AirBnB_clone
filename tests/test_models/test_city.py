#!/usr/bin/python3
""" Module contains test cases for City class
"""
import unittest
import time
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """ City Test Class
    """
    def test_instance(self):
        """ Tests if an instance is created successfully
        """
        obj_a = City()
        obj_b = City()
        self.assertIsInstance(obj_a, City)
        self.assertIsInstance(obj_b, City)
        self.assertTrue(hasattr(obj_a, 'id'))
        self.assertTrue(hasattr(obj_a, 'created_at'))
        self.assertTrue(hasattr(obj_a, 'updated_at'))
        self.assertTrue(hasattr(City, 'name'))
        self.assertTrue(hasattr(City, 'state_id'))
        self.assertIs(type(obj_a.id), str)
        self.assertIs(type(obj_a.created_at), datetime)
        self.assertIs(type(obj_a.updated_at), datetime)
        self.assertNotEqual(obj_a.id, obj_b.id)

    def test_kwargs_instance(self):
        """ Tests a successful instance when dictionary is passed
        """
        obj = City()
        obj_dict = obj.to_dict()
        new_obj = City(**obj_dict)
        self.assertIsInstance(new_obj, City)
        self.assertTrue(hasattr(new_obj, 'id'))
        self.assertTrue(hasattr(new_obj, 'created_at'))
        self.assertTrue(hasattr(new_obj, 'updated_at'))
        self.assertFalse(hasattr(new_obj, '__class_'))
        self.assertIs(type(new_obj.id), str)
        self.assertIs(type(new_obj.created_at), datetime)
        self.assertIs(type(new_obj.updated_at), datetime)
        self.assertIsNot(new_obj, obj)

    def test_string(self):
        """ Tests the __str__ method
        """
        obj = City()
        expected_str = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"

    def test_save(self):
        """ Checks the values of updated_at
        """
        obj = City()
        orig_updated_at = obj.updated_at
        time.sleep(1)
        obj.save()
        self.assertNotEqual(obj.updated_at, orig_updated_at)

    def test_to_dict(self):
        """ Tests the dictionary represenation of the object
        """
        obj = City()
        expected_dict = {
                'id': obj.id,
                'created_at': obj.created_at.isoformat(),
                'updated_at': obj.updated_at.isoformat(),
                '__class__': 'City',
                }
        self.assertEqual(obj.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
