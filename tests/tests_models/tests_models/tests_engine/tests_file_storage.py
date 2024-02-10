import unittest
import os
from unittest.mock import patch, MagicMock
from pathlib import Path
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Creates temporary file for testing."""
        cls.file_path = Path("test_file.json")
        cls.file_path.touch()

    @classmethod
    def tearDownClass(cls):
        """Removes temporary file after testing."""
        cls.file_path.unlink()

    def setUp(self):
        """Mocks and prepares for each test."""
        self.storage = FileStorage()
        self.base_model1 = BaseModel(name="John")
        self.base_model2 = BaseModel(name="Alice")

    def tearDown(self):
        """Resets and cleans up after each test."""
        self.storage.reload()  # Ensure clean state for next test

    def test_init(self):
        """Tests FileStorage initialization."""
        self.assertEqual(self.storage.__file_path, "file.json")  # Default file
        self.assertEqual(self.storage.__objects, {})  # Empty dictionary

        # Custom file
        storage_custom = FileStorage("custom_file.json")
        self.assertEqual(storage_custom.__file_path, "custom_file.json")

    def test_all(self):
        """Tests FileStorage.all() method."""
        self.storage.new(self.base_model1)
        self.storage.new(self.base_model2)

        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 2)
        self.assertIn(f"BaseModel.{self.base_model1.id}", all_objects)
        self.assertIn(f"BaseModel.{self.base_model2.id}", all_objects)

    def test_new(self):
        """Tests FileStorage.new() method."""
        self.storage.new(self.base_model1)
        self.storage.new(self.base_model2)

        self.assertIn(f"BaseModel.{self.base_model1.id}", self.storage.__objects)
        self.assertIn(f"BaseModel.{self.base_model2.id}", self.storage.__objects)
        self.assertEqual(self.storage.all()[f"BaseModel.{self.base_model1.id}"], self.base_model1)
        self.assertEqual(self.storage.all()[f"BaseModel.{self.base_model2.id}"], self.base_model2)

    def test_save(self):
        """Tests FileStorage.save() method."""
        with patch.object(open, "open", MagicMock()) as mock_open:
            self.storage.new(self.base_model1)
            self.storage.save()

            mock_open.assert_called_once_with(self.storage.__file_path, "w")
            mock_file = mock_open.return_value.__enter__.return_value
            mock_file.write.assert_called_once_with(json.dumps(self.storage.__objects))

    @patch("os.path.exists")
    def test_reload(self, mock_exists):
        """Tests FileStorage.reload() method."""
        mock_exists.return_value = True
        with patch.object(open, "open", MagicMock()) as mock_open:
            self.storage.reload()

            mock_open.assert_called_once_with(self.storage.__file_path, "r")
            mock_file = mock_open.return_value.__enter__.return_value
            mock_file.read.assert_called_once()

        mock_exists.return_value = False  # No file
        self.storage.reload()  # Should handle gracefully
        self.assertEqual(self.storage.__objects, {})

    def test_save_with_exception(self):
        """Tests FileStorage.save() with an exception."""
        with patch.object(open, "open", side_effect=Exception):
