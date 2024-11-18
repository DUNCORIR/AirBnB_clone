#!/usr/bin/python3

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City model."""

    def setUp(self):
        """Set up a new City instance for testing."""
        self.city = City()

    def test_attributes_exist(self):
        """Test that City attributes exist."""
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "state_id"))

    def test_default_values(self):
        """Test default values of the City attributes."""
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")


if __name__ == "__main__":
    unittest.main()
