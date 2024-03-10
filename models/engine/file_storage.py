#!/usr/bin/python3

import json
from models.base_model import BaseModel


class FileStorage:
    """Provides persistent storage for objects using a JSON file."""

    __file_path = "file.json"  # Path to the storage file
    __objects = {}  # In-memory cache of stored objects

    def all(self):
        """Returns a dictionary of all stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Saves all objects to the JSON file."""
        with open(FileStorage.__file_path, 'w') as file:
            json.dump({key: obj.to_dict()  # Break after to_dict()
                   for key, obj in FileStorage.__objects.items()}, file)

    def reload(self):
        """Reloads objects from the JSON file,the file doesn't exist."""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)  # Recreate class dynamically
                    obj = cls(**value)  # Instantiate object from dictionary
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
