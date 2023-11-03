#!/usr/bin/python3
"""
This script defines a class called "Base"
that serves as a base for other classes.
The "Base" class manages an instance counter and assigns
a unique identifier to each created instance.
"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    This class provides a basic structure for other classes.
    It includes methods for converting instances to dictionaries,
    updating the last modification time, and generating unique IDs.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the class.
        Assigns a unique ID and creation timestamp.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance.
        """

        class_name = self.__class__.__name__
        string = "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
        return string

    def save(self):
        """
        This method makes an update of the attribute updated_at
        """

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        This method returns the dictionary
        representation of an instance
        """

        dico = {}
        for key, value in self.__dict__.items():
            if key == 'created_at':
                dico[key] = self.created_at.isoformat()
            elif key == 'updated_at':
                dico[key] = self.updated_at.isoformat()
            else:
                dico[key] = value
        dico['__class__'] = self.__class__.__name__
        return dico
