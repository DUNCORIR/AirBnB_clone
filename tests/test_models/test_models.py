#!/usr/bin/python3

import unittest
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def test_inheritance(self):
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")


class TestCity(unittest.TestCase):
    def test_inheritance(self):
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


class TestAmenity(unittest.TestCase):
    def test_inheritance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


class TestPlace(unittest.TestCase):
    def test_inheritance(self):
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_attributes(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])


class TestReview(unittest.TestCase):
    def test_inheritance(self):
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
