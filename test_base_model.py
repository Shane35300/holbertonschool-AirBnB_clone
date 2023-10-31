#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model.name)
print(my_model.my_number)
print(my_model.id)
print(my_model.__dict__)
