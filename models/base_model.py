#!/usr/bin/python3

import pydantic
import uuid
from datetime import datetime

class BaseModel(pydantic.BaseModel):
    id: str = pydantic.Field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = pydantic.Field(default_factory=datetime.now)
    updated_at: datetime = pydantic.Field(default_factory=datetime.now)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        data = self.__dict__.copy()
        data["__class__"] = self.__class__.__name__
        data["created_at"] = data["created_at"].isoformat()
        data["updated_at"] = data["updated_at"].isoformat()
        return data

# Example usage (assuming you have other models inheriting from BaseModel):
class MyModel(BaseModel):
    name: str

model = MyModel(name="Example")
print(model)  # Output: "[MyModel] (87ba2c39-2024-02-08T10:16:29.459760)"
print(model.to_dict())  # Output: {
#    "__class__": "MyModel",
#    "id": "87ba2c39-2024-02-08T10:16:29.459760",
#    "name": "Example",
#    "created_at": "2024-02-08T10:16:29.459760",
#    "updated_at": "2024-02-08T10:16:29.459760"
# }

# Update some fields, save, and check the to_dict output
model.name = "Updated Name"
model.save()
print(model.to_dict())  # Output: {
#    "__class__": "MyModel",
#    "id": "87ba2c39-2024-02-08T10:16:29.459760",
#    "name": "Updated Name",
#    "created_at": "2024-02-08T10:16:29.459760",
#    "updated_at": "2024-02-08T10:16:29.459760"
# }
