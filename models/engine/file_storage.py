#!/usr/bin/python3
"""
This class provides a storage system for
serializing and deserializing instances
to/from a JSON file.
"""


import json


class FileStorage:
    """
    This class represents a storage system for
    serializing and deserializing instances to/from
    a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary containing all stored objects.
        """

        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.
        """

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the objects to a JSON file at the specified path.
        """

        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes objects from the JSON file to populate the storage.
        """

        from models.base_model import BaseModel

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
