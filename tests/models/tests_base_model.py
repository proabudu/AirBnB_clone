#!/usr/bin/python3

import unittest
import sys
from models.base_model import BaseModel




class TestBaseModel(unittest.TestCase):
    """This class tests the BaseModel class"""

    def setUp(self):
        """This method creates an instance of BaseModel for each test"""
        self.user = BaseModel()

    def test_init(self):
        """This method tests the initialization of the instance attributes"""
        self.assertEqual(self.user.profile["active"], False)
        self.assertEqual(self.user.profile["level"], 1)
        self.assertEqual(self.user.profile["points"], 0)

    def test_activate(self):
        """This method tests the activate method"""
        self.user.activate()
        self.assertEqual(self.user.profile["active"], True)

    def test_is_active(self):
        """This method tests the is_active method"""
        self.assertFalse(self.user.is_active())
        self.user.activate()
        self.assertTrue(self.user.is_active())

    def test_get_level(self):
        """This method tests the get_level method"""
        self.assertEqual(self.user.get_level(), 1)
        self.user.add_points(250)
        self.assertEqual(self.user.get_level(), 2)
        self.user.add_points(100)
        self.assertEqual(self.user.get_level(), 3)

    def test_get_points(self):
        """This method tests the get_points method"""
        self.assertEqual(self.user.get_points(), 0)
        self.user.add_points(50)
        self.assertEqual(self.user.get_points(), 50)

    def test_add_points(self):
        """This method tests the add_points method"""
        self.user.add_points(100)
        self.assertEqual(self.user.profile["points"], 100)
        self.user.add_points(-50)
        self.assertEqual(self.user.profile["points"], 50)

if __name__ == "__main__":
    unittest.main()
