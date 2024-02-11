#!/usr/bin/python3

"""Console module for the HBNB project."""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class that contains the command interpreter."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty line + ENTER."""
        pass

    def do_help(self, arg):
        """Show help for commands."""
        cmd.Cmd.do_help(self, arg)

    # Add more commands and methods as needed

if __name__ == '__main__':
    HBNBCommand().cmdloop()
