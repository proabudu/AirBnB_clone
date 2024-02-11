#!/usr/bin/python3

import unittest
from unittest.mock import patch, mock_open
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
   """Test cases for FileStorage class."""

   def setUp(self):
       """Set up method to create an instance of FileStorage."""
       self.storage = FileStorage()

   def tearDown(self):
       """Tear down method to delete the instance of FileStorage."""
       del self.storage

   def test_all(self):
       """Test the all method of FileStorage."""
       self.assertIsInstance(self.storage.all(), dict)

   @patch('models.engine.file_storage.json.dump')
   def test_save(self, mock_dump):
       """Test the save method of FileStorage."""
        obj = type('TestObj', (object,), {'id': '123', 'to_dict': lambda: {}})()
       self.storage.new(obj)
       self.storage.save()
       mock_dump.assert_called_once()

   @patch('models.engine.file_storage.json.load')
   def test_reload(self, mock_load):
       """Test the reload method of FileStorage."""
       mock_load.return_value = {'TestObj.123': {}}
       self.storage.reload()
       self.assertIn('TestObj.123', self.storage.all())

   @patch('models.engine.file_storage.open', new_callable=mock_open)
   def test_save_exception(self, mock_open):
       """Test save method exception handling."""
       mock_open.side_effect = Exception("Mocked open() exception")
       # Exception should not raise
       self.storage.save()

   @patch('models.engine.file_storage.open', new_callable=mock_open)
   def test_reload_exception(self, mock_open):
       """Test reload method exception handling."""
       mock_open.side_effect = FileNotFoundError("Mocked file not found")
       # Exception should not raise
       self.storage.reload()


if __name__ == "__main__":
   unittest.main()
