#!/usr/bin/python3

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity model."""

    def setUp(self):
        """Set up a new Amenity instance for testing."""
        self.amenity = Amenity()

    def test_attributes_exist(self):
        """Test that Amenity attributes exist."""
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_default_values(self):
        """Test the default value of the name attribute."""
        self.assertEqual(self.amenity.name, "")


if __name__ == "__main__":
    unittest.main()
