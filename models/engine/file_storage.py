#!/usr/bin/python3

import json
from os import path


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

   def save(self):
    with open(FileStorage.__file_path, 'w') as f:
      json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
              try:
                loaded_objects = json.load(file)
                FileStorage.__objects = {k: globals()[k.split('.')[0]](**v)
                                        for k, v in loaded_objects.items()}
              except json.JSONDecodeError:
                    pass
