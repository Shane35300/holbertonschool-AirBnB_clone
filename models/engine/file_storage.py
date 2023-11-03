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

    def all(self, cls=None):
        """
        Returns a dictionary containing all stored objects.
        """

        if cls:
            # Filter objects based on the cls argument
            filtered_objects = {key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)}
            return filtered_objects
        else:
            return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.
        """

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

        if obj.__class__.__name__ == 'User':
            email = obj.email
            duplicates = [k for k, v in self.__objects.items() if v.__class__.__name__ == 'User' and v.email == email]

            if len(duplicates) > 1:
                # There are duplicates, remove all but the most recently created instance
                for duplicate in duplicates[:-1]:
                    del self.__objects[duplicate]

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
        from models.user import User

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
                    if class_name == "User":
                        self.__objects[key] = User(**value)
        except FileNotFoundError:
            pass
