#!/usr/bin/python3

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User model."""

    def test_user_attributes(self):
        """Test that User attributes exist and have correct defaults."""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")


if __name__ == "__main__":
    unittest.main()
