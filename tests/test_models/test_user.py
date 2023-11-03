#!/usr/bin/python3
"""
Unit tests for the User class.
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def test_user_creation(self):
        """ Test creation of User instance
        """
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        """ Test User attributes
        """
        user = User()
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_str_method(self):
        """ Test the __str__ method
        """
        user = User()
        user_str = str(user)
        self.assertTrue(user_str)
        self.assertIn(user.__class__.__name__, user_str)
        self.assertIn(user.id, user_str)

    def test_to_dict_method(self):
        """ Test to_dict method
        """
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict["id"], user.id)
        self.assertEqual(user_dict["created_at"], user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"], user.updated_at.isoformat())
        self.assertEqual(user_dict["__class__"], "User")

    def test_save_method(self):
        """ Test save method
        """
        user = User()
        original_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(user.updated_at, original_updated_at)


if __name__ == "__main__":
    unittest.main()
