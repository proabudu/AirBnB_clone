import unittest
from base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_instantiation(self):
        """Test that a new instance is created with correct attributes."""
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.id, str)
        self.assertIsNotNone(model.created_at)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsNotNone(model.updated_at)
        self.assertIsInstance(model.updated_at, datetime)

    def test_string_representation(self):
        """Test that the __str__ method returns the expected string."""
        model = BaseModel()
        expected_str = f"[<class name>: BaseModel] (<ID>: {model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)

    def test_save_method(self):
        """Test that the save method updates the updated_at timestamp."""
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, original_updated_at)
        self.assertLess(original_updated_at, model.updated_at)

    def test_to_dict_method(self):
        """Test that the to_dict method returns the expected dictionary."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], model.id)
        self.assertEqual(model_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], model.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
