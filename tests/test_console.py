#!/usr/bin/python3

"""Test file for HBNBCommand class."""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """This class contains unit tests for the HBNBCommand class."""

    def setUp(self):
        """Create an instance of HBNBCommand for each test."""
        self.cmd = HBNBCommand()

    def tearDown(self):
        """Delete the instance of HBNBCommand after each test."""
        del self.cmd

    def test_do_quit(self):
        """Test the do_quit method of HBNBCommand."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(self.cmd.do_quit(''))
            self.assertEqual(output.getvalue(), '')

    def test_do_EOF(self):
        """Test the do_EOF method of HBNBCommand."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(self.cmd.do_EOF(''))
            self.assertEqual(output.getvalue(), '')

    def test_emptyline(self):
        """Test the emptyline method of HBNBCommand."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(self.cmd.emptyline())
            self.assertEqual(output.getvalue(), '')

    def test_do_help(self):
        """Test the do_help method of HBNBCommand."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(self.cmd.do_help(''))
            self.assertIn('Documented commands', output.getvalue())

    # Add more tests and methods as needed


if __name__ == "__main__":
    unittest.main()
