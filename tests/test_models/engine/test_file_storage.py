#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage
import os

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Create a temporary test file for storage
        self.file_path = "test_file.json"
        storage._FileStorage__file_path = self.file_path
        self.storage = storage
        self.test_user = User()

    def tearDown(self):
        # Clean up the temporary test file
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        # Test the 'all' method
        all_objects = self.storage.all()
        self.assertEqual(type(all_objects), dict)

    def test_new(self):
        # Test the 'new' method
        user_count = len(self.storage.all(User))
        new_user = User()
        new_user.save()
        self.assertEqual(len(self.storage.all(User)), user_count + 1)

    def test_save_reload(self):
        # Test the 'save' and 'reload' methods
        new_user = User()
        new_user.save()
        self.storage.save()
        storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertEqual(len(self.storage.all(User)), 1)

if __name__ == '__main__':
    unittest.main()
