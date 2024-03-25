#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

""" Updating FileStorage """

class_storage = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "Amenity": Amenity,
        "City": City,
        "Review": Review,
        "State": State
        }


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return (self.__objects)

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        else:
            self.__objects = {}

    for key, value in self.__objects.items():
        cls_name, id = key.split(".")
        cls = cls_upadte[cls_name]
    self.__objects[key] = cls(**value)
