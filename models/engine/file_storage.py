#!/usr/bin/python3
"""
FileStorage Class that serializes instances of to a
JSON file and deserializes JSON file to instances.
"""
import json
from models.base_model import BaseModel
from os import path
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.user import User


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances.

    Attributes:
             __file_path (str): Path to the JSON file.
             __objects (dict): Stores all objects in <class name>.id format.

    """

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
        """
        Returns the disctionary __objects.

        Returns:
            dict: The dictionary containing all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """Sets obj in __objects with key <obj class name>.id.

        Args:
            obj (BaseModel): The object to store.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file.
        (path: __file_path).
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(
                {key: obj.to_dict() for key, obj in self.__objects.items()}, f
            )

    def reload(self):
        """
        Deserializes the JSON file to __objects, if it exists.

        If the file does not exist or is invalid, no exception is raised.
        """
        if path.exists(self.__file_path):
            try:
                with open(self.__file_path, "r", encoding="utf-8") as f:
                    obj_dict = json.load(f)
                    for key, value in obj_dict.items():
                        class_name = value.get("__class__")
                        if class_name in self.class_map:
                            self.__objects[key] = (
                                    self.class_map[class_name](**value)
                            )
            except (json.JSONDecodeError, KeyError):
                # Gracefully handle invalid JSON or missing "__class__"
                pass
