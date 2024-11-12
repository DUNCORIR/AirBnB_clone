#!/usr/bin/python3
"""
The script serializes instances of to a JSON file and
deserializes JSON file to instances.
"""
import json
from models.base_model import BaseModel
import os


class FileStorage:
    """Handles file_based storage foa all models."""

    # Private class attributes
    __file_path = "file.json"  # path to JSON file for storing
    __objects = {}  # Dict to store all objects.

    # Public instance methods
    def all(self):
        """Returns the disctionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets obj in __objects with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file."""
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects, if it exists."""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
