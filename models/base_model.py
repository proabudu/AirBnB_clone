#!/usr/bin/python3

from datetime import datetime
import uuid

from pydantic import BaseModel, validator, constr

class BaseModel(BaseModel):
    """Base class for all application models. Provides common attributes, methods, and data
    validation for consistent and robust model management.

    Args:
        **kwargs (dict): A dictionary of model attribute values.
    """

    id: str = validator(
        "id", default_factory=lambda: str(uuid.uuid4()), description="Unique identifier for the model."
    )
    created_at: datetime = validator(
        "created_at", default_factory=datetime.now, description="Datetime when the model was created."
    )
    updated_at: datetime = validator(
        "updated_at", default_factory=datetime.now, description="Datetime when the model was last updated."
    )

    def __str__(self):
        """Returns a human-readable representation of the model instance."""
        return f"[<class {self.__class__.__name__}>]" \
               f" ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the `updated_at` attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the model instance for serialization.

        Keys and values:
            - **id**: String representation of the `id` attribute.
            - **created_at**: String representation of the `created_at` attribute in ISO format.
            - **updated_at**: String representation of the `updated_at` attribute in ISO format.
            - **Other model attributes**: Their respective Python values.

        Example output:
            {'id': '123e4567-e89b-12d3-a456-426655440000',
             'created_at': '2024-02-09T22:16:22.574000',
             'updated_at': '2024-02-09T22:16:22.574000',
             'name': 'John Doe',
             'age': 30}
        """
        data = self.__dict__.copy()
        data["created_at"] = data["created_at"].isoformat()
        data["updated_at"] = data["updated_at"].isoformat()
        data["__class__"] = self.__class__.__name__
        return data

    @classmethod
    def from_dict(cls, data):
        """Creates a new model instance from a dictionary representation.

        Args:
            data (dict): A dictionary containing model attribute values in the format returned by
                         `to_dict()`.

        Returns:
            BaseModel: A new instance of the model class.
        """
        # Remove the "__class__" key before instantiation
        if "__class__" in data:
            del data["__class__"]

        # Convert "created_at" and "updated_at" back to datetime objects
        if "created_at" in data:
            data["created_at"] = datetime.fromisoformat(data["created_at"])
        if "updated_at" in data:
            data["updated_at"] = datetime.fromisoformat(data["updated_at"])

        return cls(**data)
