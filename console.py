#!/usr/bin/python3
"""
This script defines a command-line interpreter for the HBNB application.
It uses the cmd module to provide an interactive command prompt.
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    This class defines the HBNB command-line interpreter, inheriting from cmd.Cmd.
    """


    prompt = "(hbnb) "

    def help_quit(self):
        """
        Display help message for the 'quit' command.
        """
        print("Quit command to exit the program\n")

    def do_quit(self, arg):
        """
        Exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program using EOF (Ctrl+D)
        """
        print() # Print a newline for better formatting
        return True

    def emptyline(self):
        """
        Override emptyline to do nothing when an empty line is entered.
        """
        pass

    def default(self, line):
        """
        Override default to handle unrecognized commands.
        """
        print(f"Command not recognized: {line}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
