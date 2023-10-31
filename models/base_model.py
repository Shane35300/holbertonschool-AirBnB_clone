#!/usr/bin/python3
"""
This script defines a class called "Base"
that serves as a base for other classes.
The "Base" class manages an instance counter and assigns
a unique identifier to each created instance.
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    This class provides a basic structure for other classes.
    It includes methods for converting instances to dictionaries,
    updating the last modification time, and generating unique IDs.
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = self.created_at

    def __str__(self):
        class_name = self.__class__.__name__
        string = "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
        return string

    def save(self):
        """
        This method make an update of the attribute updated_at
        """
        self.updated_at = str(datetime.now())

    def to_dict(self):
        """
        This method returns the dictionary
        representation of an instance
        """

        dico = {}
        for key, value in self.__dict__.items():
            if key == 'created_at':
                created_at_datetime = datetime.fromisoformat(self.created_at)
                dico[key] = created_at_datetime.isoformat()
            elif key == 'updated_at':
                created_at_datetime = datetime.fromisoformat(self.updated_at)
                dico[key] = created_at_datetime.isoformat()
            else:
                dico[key] = value

        dico['__class__'] = self.__class__.__name__
        return dico
