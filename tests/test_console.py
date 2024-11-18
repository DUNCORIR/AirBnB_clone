#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestConsole(unittest.TestCase):

    def test_help_show(self):
        """Test that the 'help show' command produces the correct output."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue()
            self.assertIn(
                    "Show an instance of BaseModel based on its id", output
            )

    def test_create_base_model(self):
        """Test that creating a BaseModel instance works."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            # Capture the created instance ID
            instance_id = f.getvalue().strip()
            HBNBCommand().onecmd(f"show BaseModel {instance_id}")
            output = f.getvalue().strip()
            self.assertIn(f"[BaseModel] ({instance_id})", output)

    def test_show_base_model(self):
        """Test that showing an instance of BaseModel works."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            # Capture created instance
            instance_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {instance_id}")
            output = f.getvalue().strip()
            self.assertIn(f"[BaseModel] ({instance_id})", output)

    def test_invalid_show(self):
        """Test the case where the show command is invalid."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_destroy_invalid_class(self):
        """Test that destroy command handles unknown class."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy UnknownClass 12345")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_invalid_syntax(self):
        """Test update command with invalid syntax."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name or instance id missing **")

    def test_all_base_model(self):
        """Test that the all command lists all BaseModel instances."""
        # Create a BaseModel instance to ensure one exists
        new_instance = BaseModel()
        storage.new(new_instance)
        storage.save()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            output = f.getvalue().strip()
            # Checks if the created instance is listed
            self.assertIn("[BaseModel]", output)

    def test_all_empty(self):
        """
        Test that the all command returns an empty
        list when no instances exist.
        """
        storage._FileStorage__objects.clear()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "[]")


if __name__ == "__main__":
    unittest.main()
