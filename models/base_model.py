#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    """Base class for all application models  attributes and methods."""

    def __init__(self):
        """Initializes a new BaseModel instance with, and other attributes."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns a human-readable string rep of the model instance."""
        return f"[<class name>: {type(self).__name__}] (<ID>: {self.id}) {self.__dict__}"

    def save(self):
        """Updates the 'updated_at' timestamp to reflect latest changes."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Converts the model instance into a dictionary representation."""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict


# Example usage
my_model = BaseModel()
print(my_model)

# Custom behavior based on specific user/context
if my_model.__class__.__name__ == "BaseModel":
    print("It's a base model with no additional attributes!")
else:
    print("It's aextended model with custom attributes:", my_model.__dict__)
