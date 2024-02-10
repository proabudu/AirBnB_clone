import unittest
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init_with_kwargs(self):
        """
        Tests that initialization with kwargs correctly sets attributes.
        """
        kwargs = {
            "_id": "my-id",
            "created_at": "2024-02-10T20:18:00.000000",
            "updated_at": "2024-02-10T20:18:00.000000",
            "name": "John Doe"
        }

        with self.assertRaises(TypeError):
            BaseModel(**kwargs)  # Invalid type for '_id'

        kwargs["_id"] = 123  # Invalid type
        with self.assertRaises(TypeError):
            BaseModel(**kwargs)

        kwargs["_id"] = "valid-id"
        base_model = BaseModel(**kwargs)

        self.assertEqual(base_model.id, "valid-id")
        self.assertEqual(base_model.created_at, datetime.fromisoformat(kwargs["created_at"]))
        self.assertEqual(base_model.updated_at, datetime.fromisoformat(kwargs["updated_at"]))
        self.assertEqual(base_model.name, "John Doe")

    def test_init_without_kwargs(self):
        """
        Tests that initialization without kwargs sets default attributes.
        """
        base_model = BaseModel()

        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)
        self.assertEqual(len(base_model.__dict__), 3)

    def test_save(self):
        """
        Tests that the save method updates the updated_at attribute and calls storage.save().
        """
        with patch.object(BaseModel, 'storage', autospec=True) as mock_storage:
            base_model = BaseModel()
            base_model.save()

            self.assertNotEqual(base_model.created_at, base_model.updated_at)
            mock_storage.save.assert_called_once()

    def test_to_dict(self):
        """
        Tests that the to_dict method returns a correct dictionary representation.
        """
        base_model = BaseModel(name="Alice")
        base_model.updated_at = datetime.now()

        expected_dict = {
            "__class__": "BaseModel",
            "id": base_model.id,
            "created_at": base_model.created_at.isoformat(),
            "updated_at": base_model.updated_at.isoformat(),
            "name": "Alice"
        }

        actual_dict = base_model.to_dict()
        self.assertEqual(actual_dict, expected_dict)

    def test_str(self):
        """
        Tests that the __str__ method returns a formatted string representation.
        """
        base_model = BaseModel(name="Bob")
        expected_str = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        actual_str = str(base_model)
        self.assertEqual(actual_str, expected_str)

if __name__ == "__main__":
    unittest.main()
