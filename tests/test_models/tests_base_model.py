#!/usr/bin/python3

"""
Test file for BaseModel class.
"""

import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class.
    """

    def test_init(self):
        """
        Test __init__ method.
        """
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime.datetime)
        self.assertIsInstance(obj.updated_at, datetime.datetime)

    def test_str(self):
        """
        Test __str__ method.
        """
        obj = BaseModel()
        expected_str = "[{}] ({}) {}".format(
            obj.__class__.__name__, obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected_str)

    def test_save(self):
        """
        Test save method.
        """
        obj = BaseModel()
        prev_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(prev_updated_at, obj.updated_at)

    def test_to_dict(self):
        """
        Test to_dict method.
        """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_kwargs(self):
        """
        Test kwargs in __init__ method.
        """
        obj = BaseModel(id="123", created_at="2022-01-01T00:00:00.000000",
                        updated_at="2022-01-01T00:00:00.000000")
        self.assertEqual(obj.id, "123")
        self.assertEqual(obj.created_at,
                         datetime.datetime(2022, 1, 1, 0, 0, 0))
        self.assertEqual(obj.updated_at,
                         datetime.datetime(2022, 1, 1, 0, 0, 0))


if __name__ == '__main__':
    unittest.main()
