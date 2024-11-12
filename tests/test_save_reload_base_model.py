#!/usr/bin/python3
"""
Unittest for storing the first object in FileStorage.
"""

import unittest
import os
import json
from models.base_model import BaseModel
from models import storage

class TestFileStorage(unittest.TestCase):
    """Test cases for storing the first object in FileStorage."""

    def setUp(self):
        """Set up the environment for testing by removing file.json if it exists."""
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """Clean up after test by removing file.json if it exists."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_store_first_object(self):
        """Test storing the first object in FileStorage."""
        # Create a new BaseModel instance and set attributes
        my_first_model = BaseModel()
        my_first_model.name = "First Model"
        my_first_model.my_number = 1
        my_first_model.save()  # Save the object to file.json

        # Check if file.json exists
        self.assertTrue(os.path.exists(self.file_path), "file.json was not created")

        # Load data from file.json
        with open(self.file_path, "r") as f:
            data = json.load(f)
        
        # Verify the object was saved with the correct key
        key = f"BaseModel.{my_first_model.id}"
        self.assertIn(key, data, "Saved object key not found in file.json")

        # Verify the object's attributes
        saved_object = data[key]
        self.assertEqual(saved_object["id"], my_first_model.id, "ID does not match")
        self.assertEqual(saved_object["name"], "First Model", "Name does not match")
        self.assertEqual(saved_object["my_number"], 1, "my_number does not match")
        self.assertIn("created_at", saved_object, "created_at not saved")
        self.assertIn("updated_at", saved_object, "updated_at not saved")

if __name__ == "__main__":
    unittest.main()
