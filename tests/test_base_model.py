#!/usr/bin/python3
"""Test cases for BaseModel class."""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def test_init(self):
        """Test BaseModel initialization."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_str(self):
        """Test __str__ method."""
        model = BaseModel()
        model_str = str(model)
        self.assertIn(model.id, model_str)

    def test_save(self):
        """Test save method."""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Test to_dict method."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

if __name__ == '__main__':
    unittest.main()
