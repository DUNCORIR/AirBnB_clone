#!/usr/bin/python3
"""
Unittest for BaseModel class
"""

from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_instance_creation(self):
        """Test if an instance of BaseModel is created correctly"""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertTrue(len(instance.id) > 0)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_unique_id(self):
        """Test that each BaseModel instance has a unique id"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_str_representation(self):
        """Test the __str__ representation of the BaseModel instance"""
        instance = BaseModel()
        expected_str = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(str(instance), expected_str)

    def test_save_method(self):
        """Test that the save method updates the updated_at attribute"""
        instance = BaseModel()
        original_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(instance.updated_at, original_updated_at)
        self.assertGreater(instance.updated_at, original_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method to check if it returns a
        dictionary with the correct keys and types
        """
        instance = BaseModel()
        instance.name = "My First Model"
        instance.my_number = 89
        instance_dict = instance.to_dict()

        # Check that to_dict returns a dictionary
        self.assertIsInstance(instance_dict, dict)

        # Check for expected keys
        self.assertIn("id", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)
        self.assertIn("__class__", instance_dict)
        self.assertIn("name", instance_dict)
        self.assertIn("my_number", instance_dict)

        # Check that the types are as expected
        self.assertIsInstance(instance_dict["id"], str)
        self.assertIsInstance(instance_dict["created_at"], str)
        self.assertIsInstance(instance_dict["updated_at"], str)
        self.assertIsInstance(instance_dict["__class__"], str)
        self.assertEqual(instance_dict["__class__"], "BaseModel")
        self.assertIsInstance(instance_dict["name"], str)
        self.assertIsInstance(instance_dict["my_number"], int)

        # Check that datetime fields are in ISO format
        created_at = datetime.fromisoformat(instance_dict["created_at"])
        updated_at = datetime.fromisoformat(instance_dict["updated_at"])
        self.assertIsInstance(created_at, datetime)
        self.assertIsInstance(updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
