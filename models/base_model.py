#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """Base model class."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        if (kwargs):
            for key, value in kwargs.items():
                if key != '_class_':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.
                        strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of the instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
