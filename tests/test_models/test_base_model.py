#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""


import unittest
from unittest.mock import patch
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_base_model_creation(self):
        """ Test creation of BaseModel instance
        """
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_base_model_attributes(self):
        """ Test BaseModel attributes
        """
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))

    def test_str_method(self):
        """ Test the __str__ method
        """
        model = BaseModel()
        model_str = str(model)

        self.assertTrue(model_str)
        self.assertIn(model.__class__.__name__, model_str)
        self.assertIn(model.id, model_str)

    def test_to_dict_method(self):
        """ Test to_dict method
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["id"], model.id)
        self.assertEqual(model_dict["created_at"],
                         model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"],
                         model.updated_at.isoformat())
        self.assertEqual(model_dict["__class__"], "BaseModel")

    def test_save_method(self):
        """ Test save method
        """
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, original_updated_at)


if __name__ == "__main__":
    unittest.main()
