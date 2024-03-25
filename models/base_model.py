#!/usr/bin/python3
"""."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """."""

    def __init__(self, *args, **kwargs):
        """.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self._dict_[k] = datetime.strptime(v, tform)
                else:
                    self._dict_[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """.
        """
        rdict = self._dict_.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["_class"] = self.class .name_
        return rdict

    def _str_(self):
        """."""
        clname = self._class.name_
        return "[{}] ({}) {}".format(clname, self.id, self._dict_)
