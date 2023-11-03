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
        from models.user import User


        if not line:
            print("** class name missing **")
            return
        class_name = line.split()[0]
        if class_name not in ("BaseModel", "User"):
            print("** class doesn't exist **")
        else:
            if class_name == "BaseModel":
                new_instance = BaseModel()
            if class_name == "User":
                new_instance = User()
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

        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        all_objs = storage.all()
        trap = 0
        for elems in all_objs.keys():
            elements = elems.split(".")
            if elements[1] == instance_id and elements[0] == class_name:
                trap = 1
        if trap == 1:
            objects = storage.all().values()
            for elem in objects:
                if instance_id in str(elem):
                    print(elem)

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
            all_objs = storage.all()
            trap = 0
            for elems in all_objs.keys():
                elements = elems.split(".")
                if elements[0] == class_name:
                    trap = 1
            if trap == 0:
                print("** class doesn't exist **")
                return
            objects = [str(obj) for obj in storage.all().values() if obj.__class__.__name__ == class_name]
        print(objects)

    def do_update(self, line):
        """
        Update an instance based on the class name and id by adding or updating attributes.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return
        if not args[3].startswith('"') and args[3].endswith('"'):
            attribute_value = args[3]
        if args[3].startswith('"') and args[3].endswith('"'):
            attribute_value = args[3][1:-1]


        # You can cast the attribute value to the appropriate type
        # For example, if the attribute is expected to be an integer, you can do:
        # attribute_value = int(attribute_value)

        # Check if the attribute name is not one of the restricted attributes
        if attribute_name in ("id", "created_at", "updated_at"):
            print("** attribute name is read-only **")
            return

        # Update the attribute of the instance
        instance = all_objs[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
