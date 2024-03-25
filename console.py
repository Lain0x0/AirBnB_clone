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
