#!/usr/bin/python3
"""Defines the BaseModel class."""

from datetime import datetime
import uuid
from pydantic import BaseModel as PydanticBaseModel
from models.engine.file_storage import FileStorage

storage = FileStorage()

class BaseModel(PydanticBaseModel):
    """A base model class."""

    id: str
    created_at: datetime
    updated_at: datetime

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            super().__init__(**kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return string representation of BaseModel instance."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update updated_at attribute with current datetime and save to storage."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dictionary representation of BaseModel instance."""
        dict_ = self.dict()
        dict_['__class__'] = type(self).__name__
        dict_['created_at'] = self.created_at.isoformat()
        dict_['updated_at'] = self.updated_at.isoformat()
        return dict_
