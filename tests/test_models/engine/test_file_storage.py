#!/usr/bin/python3
"""
This module defines unit tests for the FileStorage class.
"""


import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage


class TestFileStorage(unittest.TestCase):
    """
    This class defines unit tests for the FileStorage class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """

        self.storage = storage
        self.storage._FileStorage__file_path = "test_file.json"
        self.storage.reload()

    def tearDown(self):
        """
        Tear down the test environment.
        """

        self.storage._FileStorage__objects = {}
        with open("test_file.json", 'w') as f:
            f.write("{}")

    def test_all(self):
        """
        Test the 'all' method
        """

        all_objects = self.storage.all()
        self.assertEqual(type(all_objects), dict)

    def test_new(self):
        """
        Test the 'new' method
        """

        user_count = len(self.storage.all(User))
        new_user = User()
        new_user.save()
        self.assertEqual(len(self.storage.all(User)), user_count + 1)

    def test_save_reload(self):
        """
        Test the 'save' and 'reload' methods
        """

        new_user = User()
        new_user.save()
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertEqual(len(self.storage.all(User)), 1)


if __name__ == '__main__':
    unittest.main()
