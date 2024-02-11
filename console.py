#!/usr/bin/python3
"""
Console module for HBNB project.
"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for HBNB project.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        return True

    def emptyline(self):
        """
        Empty line method.
        """
        pass

    def do_create(self, arg):
        """
        Create command to create a new instance of BaseModel.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Show command to print the string representation of an instance.
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            if key not in models.storage.all():
                print("** no instance found **")
                return
            print(models.storage.all()[key])
        except KeyError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Destroy command to delete an instance.
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            if key not in models.storage.all():
                print("** no instance found **")
                return
            del models.storage.all()[key]
            models.storage.save()
        except KeyError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        All command to print all string representations of instances.
        """
        args = arg.split()
        objects = models.storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return
        try:
            class_name = args[0]
            if class_name not in models.storage.classes():
                print("** class doesn't exist **")
                return
            print([str(obj) for obj in objects.values() if obj.__class__.__name__ == class_name])
        except KeyError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Update command to update an instance attribute.
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in models.storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            if key not in models.storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            obj = models.storage.all()[key]
            setattr(obj, attr_name, attr_value)
            models.storage.save()
        except KeyError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
