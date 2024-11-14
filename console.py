#!/usr/bin/python3
"""
Command Line Interface (CLI) for the clone AirBnB.
"""
import cmd
import shlex  # For splitting command arguments safely
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


# Define BaseModel
class HBNBCommand(cmd.Cmd):
    """Command Interpreter for AirBnB Clone."""
    prompt = "(hbnb) "

    # Define classes dict at class level
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

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

    def do_help(self, arg):
        """List available commands with 'help'
        detailed help with 'help <command>'.
        """
        super().do_help(arg)

    def cmd(self, intro=None):
        """Override cmdloop to prevent exit in non-interactive mode"""
        print(intro or self.intro)  # Print intro if provided
        while True:
            try:
                if sys.stdin.isatty():  # Interactive mode
                    super().cmdloop(intro="")
                    break
                else:  # Non-interactive mode, handle inputs and stay open
                    line = sys.stdin.readline()
                    if not line:
                        break
                    self.onecmd(line.strip())
            except KeyboardInterrupt:
                # Handle Ctrl+C to re-display prompt
                print("\n(hbnb) ", end="", flush=True)
            except EOFError:
                break  # Exit loop on EOF

    def do_create(self, arg):
        """Create a new instance of class, save it, and print the id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        # create the objects and store it in storage system
        class_name = args[0]
        new_object = storage.class_map[class_name]()
        storage.new(new_object)
        storage.save()
        print(new_object.id)

    def do_show(self, arg):
        """ Show an instance of BaseModel based on its id"""
        args = arg.split()
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
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Destroy an instance based on class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"

        # Check if instance exists
        if key not in storage.all():
            print("** no instance found **")
            return

        # Delete the object from storage.
        del storage.all()[key]
        storage.save()

    def do_update(self, arg):
        """Update an instance by adding or updating attribute"""
        args = shlex.split(arg)
        if len(args) < 2:
            print("** class name or instance id missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if key not in storage.all():
            print("** no instance found **")
            return
        # Retrieve the instance and update attribute
        obj = storage.all()[key]

        # Handle multiple attribute-value pairs.
        for i in range(2, len(args), 2):
            attr_name, attr_value = args[i], args[i + 1]

            # Attempt to cast the value to an integer or float if applicable
            try:
                if hasattr(obj, attr_name):
                    attr_type = type(getattr(obj, attr_name))
                    if attr_type in [int, float]:
                        attr_value = attr_type(attr_value)
                setattr(obj, attr_name, attr_value)
            except ValueError:
                 print(f"** could not convert {attr_value} **")
                 continue
        obj.save()

    def do_all(self, arg):
        """Show all instances of a class, or all instances
        if no class specified
        """
        args = shlex.split(arg)
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        objects = storage.all()
        all_objects = [
            str(obj) for key, obj in objects.items()
            if not args or key.startswith(args[0])
        ]
        print(all_objects)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
