#!/usr/bin/python3
"""
Unittests for FileStorage class.
"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Set up test environment.
        """
        self.file_path = "file.json"
        self.storage = FileStorage()

    def tearDown(self):
        """
        Clean up test environment.
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_returns_dict(self):
        """
        Test that all() returns a dictionary.
        """
        self.assertEqual(type(self.storage.all()), dict)

    def test_new_adds_object(self):
        """
        Test that new() correctly adds an object to __objects.
        """
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save_creates_file(self):
        """
        Test that save() creates the JSON file.
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload_loads_objects(self):
        """
        Test that reload() correctly loads objects from the file.
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, new_storage.all())


if __name__ == "__main__":
    unittest.main()
