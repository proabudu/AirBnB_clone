#!/usr/bin/python3

import cmd

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
        # Add help for other custom commands here

    def emptyline(self):
        """Pass on empty lines."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
