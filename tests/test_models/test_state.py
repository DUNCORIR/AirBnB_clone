#!/usr/bin/python3

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State model."""

    def setUp(self):
        """Set up a new State instance for testing."""
        self.state = State()

    def test_attributes_exist(self):
        """Test that State attributes exist."""
        self.assertTrue(hasattr(self.state, "name"))

    def test_default_values(self):
        """Test default value of the name attribute."""
        self.assertEqual(self.state.name, "")


if __name__ == "__main__":
    unittest.main()
