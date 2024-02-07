#!/usr/bin/python3

import pydantic
import uuid
from datetime import datetime

class BaseModel(pydantic.BaseModel):
    """
    Craft unique data models, born with time & identity.
    """

    id: str = pydantic.Field(default_factory=lambda: str(uuid.uuid4()),
                              description="Globally unique ID.")
    created_at: datetime = pydantic.Field(default_factory=datetime.now,
                                         description="Birth datetime.")
    updated_at: datetime = pydantic.Field(default_factory=datetime.now,
                                         description="Last touched datetime.")

    def __str__(self):
        """
        Friendly name tag for debugging and logging.
        """
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """
        Mark yourself as changed, updating your 'last touched' time.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Speak the universal language of dictionaries to share your data.
        """
        data = self.__dict__.copy()
        data["__class__"] = self.__class__.__name__
        data["created_at"] = data["created_at"].isoformat()
        data["updated_at"] = data["updated_at"].isoformat()
        return data

    def __init__(self, *args, **kwargs):
        """
        Constructor: breathe life into a new model or revive an existing one.
        """
        super().__init__(*args, **kwargs)

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
