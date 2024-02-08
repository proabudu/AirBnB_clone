#!/usr/bin/python3

import json

class FileStorage:
    """
    Persistent object storage using JSON serialization.
    """

    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store objects in memory

    def all(self):
        """
        Returns all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Stores a new object in the storage.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes all objects to the JSON file.
        """
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """
        Deserializes the JSON file to retrieve objects.
        """
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass  # Do nothing if the file doesn't exist
