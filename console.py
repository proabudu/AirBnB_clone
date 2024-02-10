#!/usr/bin/python3
"""Entry point for the AirBnB console command interpreter."""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB clone."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Handle EOF."""
        print("^D")
        return True

    def emptyline(self):
        """Called when an empty line is entered."""
        pass

    def help_quit(self):
        """Help message for quit command."""
        print("Quit command to exit the program.")

    def help_EOF(self):
        """Help message for EOF."""
        print("EOF to exit the program.")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
