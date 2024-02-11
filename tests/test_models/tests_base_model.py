import unittest
from models.base_model import BaseModel
import datetime
import json


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_init(self):
        """
        Test the __init__ method of BaseModel.
        """
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime.datetime)
        self.assertIsInstance(base.updated_at, datetime.datetime)

    def test_str(self):
        """
        Test the __str__ method of BaseModel.
        """
        base = BaseModel()
        expected = "[BaseModel] ({}) {}".format(base.id, base.__dict__)
        self.assertEqual(str(base), expected)

    def test_save(self):
        """
        Test the save method of BaseModel.
        """
        base = BaseModel()
        old_updated_at = base.updated_at
        base.save()
        self.assertNotEqual(old_updated_at, base.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel.
        """
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertEqual(base_dict["id"], base.id)
        self.assertEqual(base_dict["created_at"],
                         base.created_at.isoformat())
        self.assertEqual(base_dict["updated_at"],
                         base.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
