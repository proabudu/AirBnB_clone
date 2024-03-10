#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_attributes(self):
        """ Test if BaseModel attributes are present """
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_save(self):
        """ Test if BaseModel save method updates 'updated_at' """
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_to_dict(self):
        """ Test if BaseModel to_dict method returns expected dictionary """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_str(self):
        """ Test if BaseModel __str__ method returns """
        model = BaseModel()
        string_representation = str(model)
        self.assertIn('BaseModel', string_representation)
        self.assertIn(model.id, string_representation)
        self.assertIn(str(model.__dict__), string_representation)


if __name__ == '__main__':
    unittest.main()
