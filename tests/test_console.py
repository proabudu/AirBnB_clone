import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from models.base_model import BaseModel
from models import storage
from console import HBNBCommand

class TestConsole(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Creates temporary BaseModel instances for testing."""
        cls.base_model1 = BaseModel(name="John")
        cls.base_model2 = BaseModel(name="Alice")
        storage.save(cls.base_model1)
        storage.save(cls.base_model2)

    @classmethod
    def tearDownClass(cls):
        """Deletes temporary BaseModel instances."""
        storage.delete(cls.base_model1)
        storage.delete(cls.base_model2)
        storage.reload()

    def setUp(self):
        """Mocks and prepares for each test."""
        self.console = HBNBCommand()
        self.stdout = StringIO()
        patch.object(sys, 'stdout', self.stdout).start()

    def tearDown(self):
        """Resets and cleans up after each test."""
        patch.object(sys, 'stdout', sys.__stdout__).stop()
        self.stdout.seek(0)
        self.stdout.truncate()

    def test_quit(self):
        """Tests the quit command."""
        self.console.do_quit("")
        self.assertEqual(self.stdout.getvalue(), "Exiting HBNB console...\n")

    def test_EOF(self):
        """Tests the EOF command."""
        self.console.do_EOF("")
        self.assertEqual(self.stdout.getvalue(), "Exiting HBNB console...\n")

    def test_help(self):
        """Tests the help command."""
        self.console.do_help("")
        expected_help = """Available commands:
* quit - Quit the program.
* help - Get help on available commands.
* create <class name> - Creates a new instance of a class.
* show <class name> <id> - Shows an instance based on class name and id.
* destroy <class name> <id> - Deletes an instance based on class name and id.
* all - Prints all string representations of all instances.
* all <class name> - Prints all string representations of a class.
* update <class name> <id> <attribute name> <attribute value> - Updates an instance.
"""
        self.assertEqual(self.stdout.getvalue(), expected_help)

    def test_emptyline(self):
        """Tests the emptyline method."""
        self.console.do_emptyline("")
        self.assertEqual(self.stdout.getvalue(), "")

    def test_create_valid(self):
        """Tests create command with valid arguments."""
        self.console.do_create("BaseModel name='NewName'")
        id = self.stdout.getvalue().strip()
        instance = storage.get(BaseModel, id)
        self.assertIsNotNone(instance)
        storage.delete(instance)

    def test_create_missing_class(self):
        """Tests create command with missing class name."""
        self.console.do_create("")
        self.assertEqual(self.stdout.getvalue(), "** class name missing **\n")

    def test_create_invalid_class(self):
        """Tests create command with invalid class name."""
        self.console.do_create("MyModel")
        self.assertEqual(self.stdout.getvalue(), "** class doesn't exist **\n")

    def test_show_valid(self):
        """Tests show command with valid arguments."""
        self.console.do_show("BaseModel {}".format(self.base_model1.id))
        expected_output = "[BaseModel] ({}) {}".format(self.base_model1.id, self.base_model1.__dict__)
        self.assertEqual(self.stdout.getvalue().strip(), expected_output)

    def test_show_missing_class(self):
        """Tests show command with missing class name."""
        self.console.do_show("")
        self.assertEqual(self.stdout.getvalue(), "** class name missing **\n")

    def test_show_invalid_class(self):
        """Tests show command with invalid class name."""
        self.console.do_show("MyModel 1234")
