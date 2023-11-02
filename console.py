#!/usr/bin/python3
"""
This script defines a command-line interpreter for the HBNB application.
It uses the cmd module to provide an interactive command prompt.
"""
import cmd
from models import storage


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

    def do_create(self, line):
        """
        Create a new instance of a specified class, save it, and print the ID.
        Usage: create <class_name>
        """

        from models.base_model import BaseModel


        if not line:
            print("** class name missing **")
            return
        class_name = line.split()[0]
        all_objs = storage.all()
        trap = 0
        for elems in all_objs.keys():
            elements = elems.split(".")
            if elements[0] == class_name:
                trap = 1
        if trap == 0:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()  # Créez une nouvelle instance de la classe
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Show the string representation of an instance based on class name and ID.
        Usage: show <class_name> <id>
        """

        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        all_objs = storage.all()
        trap = 0
        for elems in all_objs.keys():
            elements = elems.split(".")
            if elements[0] == class_name:
                trap = 1
        if trap == 0:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        for elems in all_objs.keys():
            elements = elems.split(".")
            if elements[1] == instance_id and elements[0] == class_name:
                trap = 2
        if trap == 2:
            print("{} {}".format(elements[0], elements[1]))
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Destroy an instance based on class name and ID and save the change.
        Usage: destroy <class_name> <id>
        """

        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        all_objs = storage.all()
        trap = 0
        for elems in all_objs.keys():
            elements = elems.split(".")
            if elements[0] == class_name:
                trap = 1
        if trap == 0:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        Print string representations of all instances (or based on class name).
        Usage: all [class_name]
        """

        args = line.split()
        if not args:
            objects = storage.all().values()
        else:
            class_name = args[0]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
                return
            objects = [str(obj) for obj in storage.all().values() if obj.__class__.__name__ == class_name]
        print(objects)

    def do_update(self, line):
        """
        Update an instance based on class name and ID by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """

        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3].strip('"')
        obj = storage.all()[key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
