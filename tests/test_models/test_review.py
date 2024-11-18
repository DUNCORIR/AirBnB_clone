#!/usr/bin/python3

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review model."""

    def setUp(self):
        """Set up a new Review instance for testing."""
        self.review = Review()

    def test_attributes_exist(self):
        """Test that Review attributes exist."""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_default_values(self):
        """Test default values of the Review attributes."""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")


if __name__ == "__main__":
    unittest.main()
