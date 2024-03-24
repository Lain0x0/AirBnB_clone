#!/usr/bin/python3
"""Import necessary modules"""
import json
import cmd
from models import storage
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

"""Dictionary of class names and their corresponding classes"""
class_origin = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "Amenity": Amenity,
        "City": City,
        "Review": Review,
        "State": State
        }


"""Define the HBNBCommand class, which inherits from cmd.Cmd"""


class HBNBCommand(cmd.Cmd):

    """Set the prompt to (hbnb)"""
    prompt = ("(hbnb) ")

    """Define the dont_exec method, which checks if a line is empty"""
    def dont_exec(self, line):
        if len(line) == 0:
            return False

    """Define the DO_EOF method, which exits the CLI"""
    def DO_EOF(self, line):
        """eof mode"""
        return self.DO_EOF(line)

    """Define the do_quit method, which exits the CLI"""
    def do_quit(self, line):
        """Exit the CLI."""
        return True

    """Define the do_create method, which creates a new object"""
    def do_create(self, line, **kwargs):
        """ creating command"""
        """Split the line into arguments"""
        args = line.split()

        """Check if a class name was provided"""
        if len(args) == 1:
            print(" ** class name missing ** ")
        else:
            """Get the class name and class object"""
            cls = globals()[args[0]]

            """Create a new object of the specified class"""
            obj = cls(**kwargs)

            """Add the new object to the storage engine"""
            storage.new(obj)

            """Save the changes to the storage engine"""
            storage.save()

            """Print the ID of the new object"""
            print(obj.id)

    """Define the do_show method, which shows an object"""
    def do_show(self, arg, id):
        """ Show command """
        """Parse the arguments"""
        args = parse(arg)

        """Check if a class name was provided"""
        if len(args) == 0:
            self.print_error("** class name missing **")
            return

        """Get the object from the storage engine"""
        obj = storage.get(args[0], args[1])

        """Check if the object exists"""
        if obj is None:
            self.print_error("** class doesn't exist **")
            return

        """Print the object"""
        print(obj)

    """Define the do_destroy method, which destroys an object"""
    def do_destroy(self, line):
        """Split the line into arguments"""
        class_name = line.split()

        """Check if a class name was provided"""
        if (len(class_name) < 1):
            print("** class name missing **")
        elif (class_name[0] not in class_origin):
            """Check if the class exists"""
            print("** class doesn't exist **")
        else:
            """Parse the arguments"""
            par_arg = parse(arg)

            """Check if an instance id was provided"""
            if (len(par_arg) < 2):
                print("** instance id missing **")
            else:
                """Get the object class"""
                obj_class = f"{class_name[0]}.{class_name[1]}"

                """Check if the object exists"""
                if obj_class not in storage.all().keys():
                    print("** no instance found **")
                else:
                    """Remove the object from the storage engine"""
                    storage.all().pop(class_obj)

                    """Save the changes to the storage engine"""
                    storage.save()

    """Define the do_update method, which updates an object"""
    def do_update(self, line):
        """Split the line into arguments"""
        line_arg = line.split()

        """Check if a class name was provided"""
        if len(line_arg) < 1:
            print("** class name missing **")
        else:
            """Check if the class exists"""
            if (line_arg[0] not in class_origin):
                print("** class doesn't exist **")
            elif (parse(arg) < 2):
                print("** instance id missing **")
            else:
                """Get the object from the storage engine"""
                nt = f"{line_arg[0]}.{line_arg[1]}"

                """Check if the object exists"""
                if nt not in storage.all().keys():
                    print("** no instance found **")
                elif (len(line_arg) < 3):
                    print("** attribute name missing **")
                return
                elif len(line_arg) < 4:
                    print("** value missing **")
                return
            else:
                """Set the attribute of the object"""
                setattr(storage.all()[st], line_arg[2], line_arg[3])

                """Save the changes to the storage engine"""
                storage.save()

    """ Define the do_all method """
    def do_all(self, line):
        """Parse the arguments"""
        objcts = []
        if (len(line) == 0):
            print([str(value) for key, value in storage.all().items()])
        else:
            """Get the class name"""
            class_str = parse(arg)

            """Check if the class exists"""
            if class_str[0] not in class_origin:
                print("** class doesn't exist **")
            else:
                """Get all objects of the specified class"""
                for key, value in storage.all().items():
                    cls = key.split(".")
                    if cls[0] == st[0]:
                        objcts.append(str(value))

                """Print the objects"""
                print(objcts)

    """Define the do_count method"""
    def do_count(self, line):
        """Print the count all class instances"""
        """Get the class name"""
        kcl = globals().get(line, None)

        """Check if the class exists"""
        if kcl is None:
            print("** class doesn't exist **")
            return

        """Count the number of objects of the specified class"""
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == line:
                count += 1

        """Print the count"""
        print(count)


"""If the script is run as the main program, start the CLI"""
if __name__ == '__main__':

    HBNBCommand().cmdloop()
