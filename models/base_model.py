#!/usr/bin/python3

# Importing necessary modules
import pydantic  # Importing Pydantic for defining BaseModel
import uuid  # Importing UUID for generating unique IDs
from datetime import datetime  # Importing datetime for timestamping

# Defining the BaseModel class
class BaseModel(pydantic.BaseModel):
    # Defining attributes with default values and validation rules
    id: str = pydantic.Field(default_factory=lambda: str(uuid.uuid4()))  # Generating a unique ID
    created_at: datetime = pydantic.Field(default_factory=datetime.now)  # Timestamping creation time
    updated_at: datetime = pydantic.Field(default_factory=datetime.now)  # Timestamping last update time

    # Customizing the string representation of the instance
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    # Method to update the 'updated_at' attribute with the current time
    def save(self):
        self.updated_at = datetime.now()

    # Method to convert the instance into a dictionary representation
    def to_dict(self):
        data = self.__dict__.copy()
        data["__class__"] = self.__class__.__name__  # Adding class name to the dictionary
        data["created_at"] = data["created_at"].isoformat()  # Converting creation time to ISO format
        data["updated_at"] = data["updated_at"].isoformat()  # Converting update time to ISO format
        return data

# Example usage (assuming you have other models inheriting from BaseModel):
class MyModel(BaseModel):
    name: str  # Defining an additional attribute 'name'

# Creating an instance of MyModel
model = MyModel(name="Example")

# Outputting the string representation of the model
print("String representation of the model:")
print(model)

# Converting the model to a dictionary and outputting it
print("\nDictionary representation of the model:")
print(model.to_dict())

# Updating some fields, saving, and checking the dictionary output after updating
model.name = "Updated Name"
model.save()
print("\nUpdated dictionary representation of the model:")
print(model.to_dict())
