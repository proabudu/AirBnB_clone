#!/usr/bin/python3

import pydantic
import uuid
from datetime import datetime
from __init__ import storage  # Import storage instance

# Base class for data models, imbued with time & identity
class BaseModel(pydantic.BaseModel):
    id: str = pydantic.Field(default_factory=str(uuid.uuid4()),
                              description="Unique ID for this entity.")
    created_at: datetime = pydantic.Field(default_factory=datetime.now,
                                         description="Time of creation.")
    updated_at: datetime = pydantic.Field(default_factory=datetime.now,
                                         description="Last time updated.")

    def __str__(self):
        """
        Human-readable representation for debugging & logging.
        """
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """
        Preserves changes by updating 'updated_at' and saving to storage.
        """
        self.updated_at = datetime.now()
        storage.save(self)  # Persist to file using FileStorage

    def __init__(self, *args, **kwargs):
        """
        Creates a new model or revives an existing one.
        """
        super().__init__(*args, **kwargs)  # Call parent constructor

        if kwargs:  # Reconstructing from dictionary
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:  # New model
            storage.new(self)  # Add to storage for persistence

