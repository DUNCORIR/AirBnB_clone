#!/usr/bin/python3
"""
BaseModel class for AirBnB Clone Project.
Defines all common attributes/methods for other classes.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel defines all common attributes/methods for other classes.

    Attributes:
        id (str): Unique identifier for each instance.
        created_at (datetime): Timestamp when the instance is created.
        updated_at (datetime): Timestamp for the last update on the instance.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            *args (any): Not used
            **kwargs (dict): Key /value pairs of attributes
        """

        if kwargs:
            # Remove '__class__' key if presen
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            # Standard initialization for a new instance
            self.id = str(uuid.uuid4())  # Assign unique id to self.id
            self.created_at = datetime.now()  # set to current date and time
            self.updated_at = self.created_at
            models.storage.new(self)  # only called when new instance created

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: String format of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute to current datetime.
        """
        # Links the storage engine save method in future tasks.
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        converts the instance to a dictionary format.

        Returns:
            dict: Dictionary representation of an instance.
        """
        dict_rep = {
                'id': self.id,
                'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat(),

                '__class__': self.__class__.__name__,
        }
        # Add any other attributes dynamically
        for key, value in self.__dict__.items():
            if key not in ('id', 'created_at', 'updated_at'):
                dict_rep[key] = value

        return dict_rep
