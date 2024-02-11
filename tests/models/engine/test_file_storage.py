#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """This class tests the FileStorage class"""

    def setUp(self):
        """This method creates an instance of Filel for each test"""
        self.storage = FileStorage()
        self.user = BaseModel()

    def test_all(self):
        """This method tests the all method"""
        self.assertIsInstance(self.storage.all(), dict)
        self.assertEqual(len(self.storage.all()), 0)
        self.storage.new(self.user)
        self.assertEqual(len(self.storage.all()), 1)

    def test_new(self):
        """This method tests the new method"""
        self.storage.new(self.user)
        key = "{}.{}".format(self.user.__class__.__name__, self.user.id)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], self.user)

    def test_save(self):
        """This method tests the save method"""
        self.storage.new(self.user)
        self.storage.save()
        with open(self.storage.__file_path, 'r') as file:
            data = json.load(file)
            key = "{}.{}".format(self.user.__class__.__name__, self.user.id)
            self.assertIn(key, data)
            self.assertEqual(data[key], self.user.to_dict())

    def test_reload(self):
        """This method tests the reload method"""
        self.storage.new(self.user)
        self.storage.save()
        self.storage.__objects = {}
        self.assertEqual(len(self.storage.all()), 0)
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 1)
        key = "{}.{}".format(self.user.__class__.__name__, self.user.id)
        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], BaseModel)

if __name__ == "__main__":
    unittest.main()
