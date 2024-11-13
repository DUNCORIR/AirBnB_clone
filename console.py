#!/usr/bin/python3
"""
Command Line Interface (CLI) for the clone AirBnB.
"""
import cmd
import shlex  # For splitting command arguments safely
from models.base_model import BaseModel
from models import storage


# Define BaseModel
class HBNBCommand(cmd.Cmd):
    """Command Interpreter for AirBnB Clone."""
    prompt = "(hbnb) "

    # Define classes dict at class level
    classes = {"BaseModel": BaseModel}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id"""
        if not arg:
            print("** class name missing **")
            return
        elif arg not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            obj = self.classes[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """ Show an instance of BaseModel based on its id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if instance is None:
            print("** no instance found **")
        else:
            print(instance)

    def do_all(self, arg):
        """Show all instances of a class, or all instances
        if no class specified"""
        args = shlex.split(arg)
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        objects = storage.all()
        all_objects = []
        if args:
            all_objects = [
                str(obj)
                for key, obj in objects.items()
                if key.startswith(args[0])
            ]
        else:
            # Add all objects if no class specified
            all_objects = [str(obj) for obj in obj in objects.value()]

        print(all_objects)

    def do_destroy(self, arg):
        """Destroy an instance based on class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_update(self, arg):
        """Update an instance of BaseModel by adding or updating attribute"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class doesn't exist **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if instance is None:
            print("** no instance found **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3]

        # Type cast value
        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            try:
                attr_value = attr_type(attr_value)
            except ValueError:
                print(f"** could not convert value to {attr_type.__name__} **")
                return

        setattr(instance, attr_name, attr_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
