#!/usr/bin/python3
import json
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class_origin = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "Amenity": Amenity,
        "City": City,
        "Review": Review,
        "State": State
        }


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def dont_exec(self, line):
        if len(line) == 0:
            return False

    def do_EOF(self, line):
        """eof mode"""
        return self.do_EOF(line)

    def do_quit(self, line):
        """Exit the CLI."""
        return True

    def do_create(self, line, **kwargs):
        """ creating command"""
        args = line.split()
        if len(args) == 1:
            print(" ** class name missing ** ")
        else:
            try:
                cls = globals()[args[0]]
                obj = cls(**kwargs)
                storage.new(obj)
                storage.save()
                print(obj.id)
            except NameError:
                print(" ** class doesn't exist ** ")

    def do_show(self, arg, id):
        """ Show command """
        args = parse(arg)
        if len(args) == 0:
            self.print_error("** class name missing **")
            return
        obj = storage.get(args[0], args[1])
        if obj is None:
            self.print_error("** class doesn't exist **")
            return
        print(obj)
        if len(args) != 2:
            print("** instance id missing **")
        else:
            obj = storage.get(args[0], args[1])
            if obj is None:
                print("** no instance found **")
                return
            print(obj)

    def do_destroy(self, line):
        class_name = line.split()
        if len(class_name) < 1:
            print("** class name missing **")
        elif class_name[0] not in class_origin:
            print("** class doesn't exist **")
        else:
            par_arg = parse(arg)
            if len(par_arg) < 2:
                print("** instance id missing **")
                obj_class = f"{class_name[0]}.{class_name[1]}"
                if obj_class not in storage.all().keys():
                    print("** no instance found **")
                else:
                    storage.all().pop(class_obj)
                    storage.save()

    def do_update(self, line):
        line_arg = line.split()
        if len(line_arg) < 1:
            print("** class name missing **")
        else:
            if line_arg[0] not in class_origin:
                print("** class doesn't exist **")
            elif parse(arg) < 2:
                print("** instance id missing **")
            else:
                nt = f"{line_arg[0].{line_arg[1]}}"
                if nt not in storage.all().keys():
                    print("** no instance found **")
                elif len(line_arg) < 3:
                    print("** attribute name missing **")
                    return
                elif len(line_arg) < 4:
                    print("** value missing **")
                    return
                else:
                    setattr(storage.all()[st], line_arg[2], line_arg[3])
                    storage.save()

    def do_all(self, line):
        objcts = []
        if len(line) == 0:
            print([str(value) for key, value in storage.all().items()])
        else:
            class_str = parse(arg)
            if class_str[0] not in class_origin:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    cls = key.split(".")
                    if cls[0] == st[0]:
                        objcts.append(str(value))
                print(objcts)

    def do_count(self, line):
        """Print the count all class instances"""
        kcl = globals().get(line, None)
        if kcl is None:
            print("** class doesn't exist **")
            return
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == line:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
