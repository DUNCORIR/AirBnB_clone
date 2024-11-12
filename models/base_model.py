#!/usr/bin/python3
"""
This Module classs BaseModel defines all common attributes/methods
for other classes.
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
            *args (any): Not used at moment
            **kwargs (dict): Key /value pairs of attributes
        """

        if kwargs:
            if '__class__' not in kwargs:
                # Confirm __class__ key presence
                raise KeyError("__class__key is required in dictionary")
            self.id = kwargs.get('id', str(uuid.uuid4()))
            if 'created_at' in kwargs:
                self.created_at = datetime.fromisoformat(kwargs['created_at'])
            else:
                self.created_at = datetime.now()
            if 'updated_at' in kwargs:
                self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
            else:
                self.updated_at = datetime.now()
            # Set other attributes from kwargs without __class_
            for key, value in kwargs.items():
                if key not in ['created_at', 'updated_at', '__class__']:
                    setattr(self, key, value)
        else:
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
            'my_number': self.__dict__.get('my_number'),
            'name': self.__dict__.get('name'),
            '__class__': self.__class__.__name__,
            'updated_at': self.updated_at.isoformat(),
            'id': self.id,
            'created_at': self.created_at.isoformat()
        }
        return {k: v for k, v in dict_rep.items() if v is not None}
