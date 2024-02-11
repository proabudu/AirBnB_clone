import unittest
from base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_instantiation(self):
        """Test creation of a new instance with correct attributes."""
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.id, str)
        self.assertIsNotNone(model.created_at)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsNotNone(model.updated_at)
        self.assertIsInstance(model.updated_at, datetime)

    def test_string_representation(self):
        """Test __str__ method for expected string representation."""
        model = BaseModel()
        expected_str = (
            f"[<class name>: BaseModel] (<ID>: {model.id}) {model.__dict__}"
        )
        self.assertEqual(str(model), expected_str)

    def test_save_method(self):
        """Test save method updates updated_at timestamp."""
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, original_updated_at)
        self.assertLess(original_updated_at, model.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method for expected dictionary representation."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], model.id)
        self.assertEqual(model_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], model.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
