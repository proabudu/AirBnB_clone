#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    """Base class for all models."""

    def __init__(self):
        """Initializes a new BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the model."""
        return f"[({self.id})] {type(self).__name__}: {self.__dict__}"

    def save(self):
        """Updates the updated_at timestamp."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the model."""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict


# Example usage
my_model = BaseModel()
print(my_model)  # Output: [<uuid4>] BaseModel: {'id': ..., 'created_at': ..., 'updated_at': ...}
