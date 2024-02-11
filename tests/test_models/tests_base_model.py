#!/usr/bin/python3

"""Test file for BaseModel class."""

import unittest
import datetime
from models.base_model import BaseModel
from models.engine import storage


class TestBaseModel(unittest.TestCase):
    """This class contains unit tests for the BaseModel class."""

    def setUp(self):
        """Create an instance of BaseModel for each test."""
        self.base = BaseModel()

    def tearDown(self):
        """Delete the instance of BaseModel after each test."""
        del self.base

    def test_init(self):
        """Test the __init__ method of BaseModel."""
        self.assertIsInstance(self.base, BaseModel)
        self.assertIsInstance(self.base.id, str)
        self.assertIsInstance(self.base.created_at, datetime.datetime)
        self.assertIsInstance(self.base.updated_at, datetime.datetime)

    def test_str(self):
        """Test the __str__ method of BaseModel."""
        expected = "[BaseModel] ({}) {}".format(
            self.base.id, self.base.__dict__)
        self.assertEqual(str(self.base), expected)

    def test_save(self):
        """Test the save method of BaseModel."""
        old_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(old_updated_at, self.base.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertEqual(base_dict["id"], self.base.id)
        self.assertEqual(
            base_dict["created_at"], self.base.created_at.isoformat())
        self.assertEqual(
            base_dict["updated_at"], self.base.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
