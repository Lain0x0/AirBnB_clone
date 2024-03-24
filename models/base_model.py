#!/usr/bin/python3
""" Importing Modules we need """
import uuid
from datetime import datetime
import models


class ModelBase:
    def __init__(self, *args, **kawrgs):
        """ """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if (kawrgs):
            for key, value in kawrgs.items():
                if key != "__class__":
                    setattr(self, value, kawrgs)
        else:
            self.id
            self.created_at = datetime.utcnow()

    def __str__(self):
        """ """
        print(f"[<class name>] ({self.id}) {self.__dict__}")

    def save(self):
        """ """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ """
        self.__dict__
        self.__class__
        self.created_at = datetime.isoformat()
        self.updated_at = datetime.isoformat()

        return self.__dict__
