#!/usr/bin/python3
"""Test cases for BaseModel class and FileStorage class."""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

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

class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def setUp(self):
        """Set up method for tests."""
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down method for tests."""
        self.storage = None

    def test_all(self):
        """Test all method."""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        """Test new method."""
        model = BaseModel()
        self.storage.new(model)
        all_objects = self.storage.all()
        self.assertIn('BaseModel.' + model.id, all_objects)

    # You can add more tests for save and reload methods if needed

if __name__ == '__main__':
    unittest.main()
