import cmd
from models import storage
from models.base_model import BaseModel
from datetime import datetime
import json

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the program."""
        print("Exiting HBNB console...")
        exit(0)

    def do_EOF(self, arg):
        """Quit the program on EOF."""
        print("Exiting HBNB console...")
        exit(0)

    def do_help(self, arg):
        """Prints help for available commands."""
        print("Available commands:")
        print("* quit - Quit the program.")
        print("* help - Get help on available commands.")
        print("* create <class name> - Creates a new instance of a class.")
        print("* show <class name> <id> - Shows an instance based on class name and id.")
        print("* destroy <class name> <id> - Deletes an instance based on class name and id.")
        print("* all - Prints all string representations of all instances.")
        print("* all <class name> - Prints all string representations of a class.")
        print("* update <class name> <id> <attribute name> <attribute value> - Updates an instance.")

    def emptyline(self):
        """Pass on empty lines."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        try:
            model_class = getattr(models, class_name)
            instance = model_class()
            instance.save()
            print(instance.id)
        except AttributeError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Shows an instance based on class name and id."""
        args = arg.split()
        if len(args) != 2:
            print("** class name missing **" if not args else "** instance id missing **")
            return

        class_name, instance_id = args
        try:
            model_class = getattr(models, class_name)
            instance = storage.get(model_class, instance_id)
            if instance:
                print(instance)
            else:
                print("** no instance found **")
        except AttributeError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = arg.split()
        if len(args) != 2:
            print("** class name missing **" if not args else "** instance id missing **")
            return

        class_name, instance_id = args
        try:
            model_class = getattr(models, class_name)
            instance = storage.get(model_class, instance_id)
            if instance:
                storage.delete(instance)
                print("** instance deleted **")
            else:
                print("** no instance found **")
        except AttributeError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representations of all instances."""
        args = arg.split()
        if args:
            class_name = args[0]
            try:
                model_class = getattr(models, class_name)
                instances = storage.all(model_class)
                print("[", end="")
                print(", ".join([str(instance) for instance in instances]), end="")
                print("]")
            except AttributeError:
                print("** class doesn't exist **")
        else:
            objects = storage.all()
            print("[", end="")
            print(", ".join([str(instance) for instance in objects.values()]), end="")
            print("]")

    def do_update(self, arg):
        """Updates an instance based on class name and id."""
        args = arg.split()
        if len(args) < 4:
            print("** Usage: update <class name> <id> <attribute name> <attribute value> **")
            return

        class_name, instance_id, attr_name, value = args[:4]
        try:
            model_class = getattr
