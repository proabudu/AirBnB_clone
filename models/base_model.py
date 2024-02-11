#!/usr/bin/python3

"""This module defines the BaseModel class"""

import uuid
import datetime


class BaseModel:
    """This class defines common attributes and methods for other classes"""

    def __init__(self, *args, **kwargs):
        """This method initializes the instance attributes"""

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """This method returns a string representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """This method updates the updated_at attribute with curdatetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """This method returns a dictionary representation of the object"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
