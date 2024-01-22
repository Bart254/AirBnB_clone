#!/usr/bin/python3
""" Module contains test cases for User class
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """ User Test Class
    """
    def setUp(self):
        """ Creates a User object before any test
        """
        self.obj = User()

    def test_attributes(self):
        """ Tests if objects are created with all attributes of user
        """
        self.assertIsInstance(self.obj, User)
        self.assertTrue(hasattr(self.obj, 'email'))
        self.assertTrue(hasattr(self.obj, 'password'))
        self.assertTrue(hasattr(self.obj, 'first_name'))
        self.assertTrue(hasattr(self.obj, 'last_name'))
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))


if __name__ == "__main__":
    unittest.main()
