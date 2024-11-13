#!/usr/bin/python3
"""
The script serializes instances of to a JSON file and
deserializes JSON file to instances.
"""
import json
from models.base_model import BaseModel
import os
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.user import User


class FileStorage:
    """Handles file_based storage foa all models."""

    # Private class attributes
    __file_path = "file.json"  # path to JSON file for storing
    __objects = {}  # Dict to store all objects.

    # Mapping of class names to class types
    class_map = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

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

                    # Check for all class names
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
                    elif class_name == "User":  # Check for user class
                        self.__objects[key] = User(**value)
                    elif class_name == "State":
                        self.__objects[key] = State(**value)
                    elif class_name == "City":
                        self.__objects[key] = City(**value)
                    elif class_name == "Amenity":
                        self.__objects[key] = Amenity(**value)
                    elif class_name == "Place":
                        self.__objects[key] = Place(**value)
                    elif class_name == "Review":
                        self.__objects[key] = Review(**value)
        except FileNotFoundError:
            pass
