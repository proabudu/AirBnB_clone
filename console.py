#!/usr/bin/python3
import cmd
import json
import sys
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit()

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        if arg_list[0] not in models.classes:
            print("** class doesn't exist **")
            return
        new_instance = models.classes[arg_list[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        arg_list = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if arg_list[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = arg_list[0] + "." + arg_list[1]
        all_objects = models.storage.all()
        if key in all_objects:
            print(all_objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        arg_list = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if arg_list[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = arg_list[0] + "." + arg_list[1]
        all_objects = models.storage.all()
        if key in all_objects:
            del all_objects[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        arg_list = arg.split()
        all_objects = models.storage.all()
        if not arg:
            print([str(obj) for obj in all_objects.values()])
            return
        if arg_list[0] not in models.classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in all_objects.items() if key.startswith(arg_list[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        arg_list = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if arg_list[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = arg_list[0] + "." + arg_list[1]
        all_objects = models.storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        if len(arg_list) < 4:
            print("** value missing **")
            return
        setattr(all_objects[key], arg_list[2], arg_list[3])
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
