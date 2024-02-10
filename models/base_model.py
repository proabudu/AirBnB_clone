#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4
from pydantic import BaseModel

class BaseModel(BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime

    def __init__(self, **data):
        # Generate a unique ID using uuid4 and convert it to a string
        self.id = str(uuid4())
        # Set the created_at and updated_at attributes to the current datetime
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        super().__init__(**data)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        """
        data = self.__dict__.copy()
        # Add the __class__ key with the class name
        data['__class__'] = self.__class__.__name__
        # Convert created_at and updated_at to ISO format strings
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

    def __str__(self):
        """
        Custom string representation: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

