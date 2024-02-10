import unittest
import os
import json
from unittest.mock import patch
from models.base_model import BaseModel
from models.engine import file_storage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.test_obj = BaseModel()
        self.test_obj2 = BaseModel()
        file_storage._FileStorage__objects = {}

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """
        Tests that the all() method returns all stored objects.
        """
        file_storage.new(self.test_obj)
        file_storage.new(self.test_obj2)

        all_objects = file_storage.all()

        self.assertEqual(len(all_objects), 2)
        self.assertIn(f"BaseModel.{self.test_obj.id}", all_objects)
        self.assertIn(f"BaseModel.{self.test_obj2.id}", all_objects)

    def test_new(self):
        """
        Tests that the new() method adds an object to the storage.
        """
        file_storage.new(self.test_obj)

        stored_obj = file_storage._FileStorage__objects[f"BaseModel.{self.test_obj.id}"]

        self.assertEqual(stored_obj, self.test_obj)

    def test_save(self):
        """
        Tests that the save() method serializes objects to a JSON file.
        """
        file_storage.new(self.test_obj)
        with patch.object(os, "open", return_value=mock_open()) as mock_open:
            file_storage.save()

            mock_open.assert_called_once_with("file.json", "w", encoding="utf-8")
            mock_file = mock_open.return_value
            mock_file.write.assert_called_once_with(json.dumps(file_storage._FileStorage__objects, indent=4))

    @patch("os.path.exists")
    def test_reload(self, mock_exists):
        """
        Tests that the reload() method deserializes objects from a JSON file.
        """
        mock_exists.return_value = True
        with open("file.json", "w") as f:
            json.dump({f"BaseModel.{self.test_obj.id}": self.test_obj.to_dict()}, f)

        file_storage.reload()

        self.assertEqual(
            file_storage._FileStorage__objects[f"BaseModel.{self.test_obj.id}"], self.test_obj
        )

    def test_reload_not_exists(self):
        """
        Tests that reload() does nothing if the file doesn't exist.
        """
        file_storage.reload()

        self.assertEqual(len(file_storage._FileStorage__objects), 0)

    def test_delete(self):
        """
        Tests that the delete() method removes an object from storage.
        """
        file_storage.new(self.test_obj)
        file_storage.delete(self.test_obj)

        self.assertNotIn(f"BaseModel.{self.test_obj.id}", file_storage._FileStorage__objects)

if __name__ == "__main__":
    unittest.main()
