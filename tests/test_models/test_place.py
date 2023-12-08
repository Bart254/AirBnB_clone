#!/usr/bin/python3
""" Module contains test cases for Place class
"""
import unittest
import time
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Place Test Class
    """
    def test_instance(self):
        """ Tests if an instance is created successfully
        """
        obj_a = Place()
        obj_b = Place()
        self.assertIsInstance(obj_a, Place)
        self.assertIsInstance(obj_b, Place)
        self.assertTrue(hasattr(obj_a, 'id'))
        self.assertTrue(hasattr(obj_a, 'created_at'))
        self.assertTrue(hasattr(obj_a, 'updated_at'))
        self.assertTrue(hasattr(Place, 'amenity_ids'))
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertTrue(hasattr(Place, 'name'))
        self.assertTrue(hasattr(Place, 'description'))
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertIs(type(Place.max_guest), int)
        self.assertIs(type(Place.longitude), float)
        self.assertIs(type(Place.latitude), float)
        self.assertIs(type(obj_a.created_at), datetime)
        self.assertIs(type(obj_a.updated_at), datetime)
        self.assertNotEqual(obj_a.id, obj_b.id)

    def test_kwargs_instance(self):
        """ Tests a successful instance when dictionary is passed
        """
        obj = Place()
        obj_dict = obj.to_dict()
        new_obj = Place(**obj_dict)
        self.assertIsInstance(new_obj, Place)
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
        obj = Place()
        expected_str = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"

    def test_save(self):
        """ Checks the values of updated_at
        """
        obj = Place()
        orig_updated_at = obj.updated_at
        time.sleep(1)
        obj.save()
        self.assertNotEqual(obj.updated_at, orig_updated_at)

    def test_to_dict(self):
        """ Tests the dictionary represenation of the object
        """
        obj = Place()
        expected_dict = {
                'id': obj.id,
                'created_at': obj.created_at.isoformat(),
                'updated_at': obj.updated_at.isoformat(),
                '__class__': 'Place',
                }
        self.assertEqual(obj.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
