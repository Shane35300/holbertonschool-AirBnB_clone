#!/usr/bin/python3
"""
Ce script définit une classe appelée "Base"
qui sert de base pour d'autres classes.
La classe "Base" gère un compteur d'instances et attribue
un identifiant unique à chaque instance créée.
"""

import uuid
import datetime

class BaseModel:
    """

    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.datetime.now())
        self.updated_at = self.created_at

    def __str__(self):
        class_name = self.__class__.__name__
        string = "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
        return string

    def save(self):
        self.updated_at = str(datetime.datetime.now())

    def to_dict(self):
        """
        This method returns the dictionary
        representation of an instance
        """

        dico = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                dico[key] = value.isoformat()
            else:
                dico[key] = value

        dico['__class__'] = self.__class__.__name__
        return dico
