import json
from models.base_model import BaseModel

class FileStorage:
    """Class for loading and saving objects from/to a JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all stored objects."""
        return self.__objects

    def new(self, obj):
        """Stores a new object."""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Saves all objects to the JSON file."""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Loads objects from the JSON file."""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass  # No file to load
