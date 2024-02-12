#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
    Test cases for the HBNBCommand class in console.py.
    """

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        """
        Test quit command.
        """
        with patch('builtins.input', return_value="quit"):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        """
        Test EOF command.
        """
        with patch('builtins.input', side_effect=["EOF"]):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        """
        Test empty line input.
        """
        with patch('builtins.input', return_value=""):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        """
        Test create command.
        """
        with patch('builtins.input', side_effect=["create BaseModel"]):
            HBNBCommand().cmdloop()
            self.assertTrue(len(mock_stdout.getvalue()) > 0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        """
        Test show command.
        """
        with patch('builtins.input', side_effect=["show BaseModel", "EOF"]):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), '** instanmissing **\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        """
        Test destroy command.
        """
        with patch('builtins.input', side_effect=["destroyBaseModel", "EOF"]):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), '** instancissing **\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        """
        Test all command.
        """
        with patch('builtins.input', side_effect=["all BaseModel", "EOF"]):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), '** oesn\'t exist **\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        """
        Test update command.
        """
        with patch('builtins.input', side_effect=["update BaseModel", "EOF"]):
            HBNBCommand().cmdloop()
            self.assertEqual(mock_stdout.getvalue(), '** instaeidising **\n')


if __name__ == '__main__':
    unittest.main()
