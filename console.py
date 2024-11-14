#!/usr/bin/python3
"""
Command Line Interface (CLI) for the clone AirBnB.
"""
import ast  # For safely parsing dictionaries
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
        # Construct the key for storage
        key = f"{args[0]}.{args[1]}"

        # Check if instance exists
        if key not in storage.all():
            print("** no instance found **")
            return

        # Delete the object/instance from storage.
        del storage.all()[key]
        storage.save()

    def do_update(self, arg):
        """Update an instance by adding or updating attributes.Supports
        both single attribute-value updates and dictionary-based updates.
        """
        args = shlex.split(arg)
        # Check if we have at least a class name and an instance ID
        if len(args) < 2:
            print("** class name or instance id missing **")
            return
        # Check if the class name is valid
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        # Construct the key for the instance
        key = f"{args[0]}.{args[1]}"
        # Check if the instance exists
        if key not in storage.all():
            print("** no instance found **")
            return
        # Retrieve the instance and update attribute
        obj = storage.all()[key]

        # Check if the argument is a dictionary (3rd argument)
        if len(args) == 3:
            try:
                #  Try parse string 3rd arg as a dictionary safely
                attributes = ast.literal_eval(args[2])  # safe parse
                if isinstance(attributes, dict):
                    # Update the object using dictionary values
                    for attr_name, attr_value in attributes.items():
                        if hasattr(obj, attr_name):
                            attr_type = type(getattr(obj, attr_name))
                            if attr_type in [int, float]:
                                attr_value = attr_type(attr_value)
                        setattr(obj, attr_name, attr_value)
                    obj.save()
                    return
            except (SyntaxError, ValueError):
                print("** invalid dictionary format **")
                return

        # Handle single attribute-value pair updates
        if len(args) < 4:
            print("** attribute name or value missing **")
            return

        # Handle multiple attribute-value updates
        for i in range(2, len(args), 2):
            if i + 1 >= len(args):  # Ensures no out of range
                print("** value missing **")
                return
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

    def default(self, line):
        """ Handles commands with <class name>.command() format."""
        args = line.split(".")
        if len(args) == 2:
            class_name, command = args[0], args[1]
            if class_name in self.classes:
                # Handle <class name>.create() command
                if command == "create()":
                    self.do_create(class_name)
                # Handle <class name>.all() command
                elif command == "all()":
                    # Calling do_all with the class name
                    self.do_all(class_name)
                # Handle <class name>.count() command
                elif command == "count()":
                    self.do_count(class_name)
                # Handle <class name>.show(<id>) command
                elif command.startswith("show(") and command.endswith(")"):
                    # Extract the ID/strip any surrounding quotes
                    instance_id = command[5:-1].strip("\"'")
                    self.do_show(f"{class_name} {instance_id}")
                # Handle <class name>.destroy(<id>) command
                elif command.startswith("destroy(") and command.endswith(")"):
                    instance_id = command[8:-1].strip("\"'")
                    self.do_destroy(f"{class_name} {instance_id}")
                # <class name>.update(<id>,<attribute name>,<attribute value>
                elif command.startswith("update(") and command.endswith(")"):
                    update_args = command[7:-1].split(", ", 2)

                    # Check if the second argument is a dictionary
                    if len(update_args) == 2:
                        instance_id = update_args[0].strip("\"'")
                        try:
                            # Attempt to parse the 2nd arg as a dict.
                            attributes = ast.literal_eval(
                                    update_args[1].strip()
                            )
                            if isinstance(attributes, dict):
                                # For each key-value pair, call do_update
                                for attr_name, attr_value in attr.items():
                                    self.do_update(
                                            f"{class_name} {instance_id} "
                                            f"{attribute_name} "
                                            f"{attribute_value} "
                                    )
                                return
                        except (SyntaxError, ValueError):
                            print("** invalid dictionary syntax **")
                            return
                    # <class name>.update(<id>,<attr name>,<attr value>
                    elif len(update_args) == 3:
                        instance_id = update_args[0].strip("\"'")
                        attribute_name = update_args[1].strip("\"'")
                        attribute_value = update_args[2].strip("\"'")
                        self.do_update(
                                f"{class_name} {instance_id} "
                                f"{attribute_name} "
                                f"{attribute_value} "
                        )
                    else:
                        print(f"** invalid syntax **")
                else:
                    print("*** Unknown syntax: {line}")
            else:
                print("** class doesn't exist **")
        else:
            print(f"** Unknown syntax: {line}")

    def do_count(self, class_name):
        """Counts instances of a specific class."""
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        objects = storage.all()
        count = sum(1 for key in objects if key.startswith(class_name))
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
