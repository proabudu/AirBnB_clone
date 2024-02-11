#!/usr/bin/python3
"""This module defines the BaseModel class"""

import uuid
import datetime

class BaseModel:
    """This class defines the common attributes and methods for other classes"""

    def __init__(self, **kwargs):
        """This method initializes the instance attributes"""
        self.id = str(uuid.uuid4()) # generate a unique id as a string
        self.created_at = datetime.datetime.now() # assign the current datetime
        self.updated_at = datetime.datetime.now() # assign the current datetime
        # assign any other attributes from kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """This method returns a string representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """This method updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """This method returns a dictionary representation of the object"""
        # copy the instance dictionary
        obj_dict = self.__dict__.copy()
        # add the __class__ key with the class name
        obj_dict["__class__"] = self.__class__.__name__
        # convert the datetime attributes to strings in ISO format
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
