import unittest
import sys
import os
from unittest.mock import MagicMock
from uuid import uuid4

# Ajouter le répertoire parent de `tests_api` au `sys.path`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Ajouter le répertoire `tests_api` au `sys.path`
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from data_manager import DataManager
from model.place import Place
from model.user import User
from model.review import Review
from model.amenity import Amenity
from model.country import Country
from model.city import City

class DataManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()

        # Mock repositories
        self.data_manager.place_repository = MagicMock()
        self.data_manager.user_repository = MagicMock()
        self.data_manager.review_repository = MagicMock()
        self.data_manager.amenity_repository = MagicMock()
        self.data_manager.country_repository = MagicMock()
        self.data_manager.city_repository = MagicMock()

    # Tests for Place
    def test_save_place(self):
        place_data = {
            'name': 'Test Place',
            'description': 'A nice place',
            'address': '123 Main St',
            'city_id': 'city_123',
            'latitude': 40.7128,
            'longitude': -74.0060,
            'host_id': 'host_123',
            'number_of_rooms': 3,
            'number_of_bathrooms': 2,
            'price_per_night': 150,
            'max_guests': 4,
            'amenity_ids': ['amenity_1', 'amenity_2']
        }
        place_id = 'place_123'
        self.data_manager.place_repository.save.return_value = place_id

        result = self.data_manager.save_place(place_data)
        self.data_manager.place_repository.save.assert_called_once()
        self.assertEqual(result, place_id)

    def test_get_place(self):
        place_id = 'place_123'
        place_data = {
            'name': 'Test Place',
            'description': 'A nice place',
            'address': '123 Main St',
            'city_id': 'city_123',
            'latitude': 40.7128,
            'longitude': -74.0060,
            'host_id': 'host_123',
            'number_of_rooms': 3,
            'number_of_bathrooms': 2,
            'price_per_night': 150,
            'max_guests': 4,
            'amenity_ids': ['amenity_1', 'amenity_2']
        }
        place = Place(place_id=place_id, **place_data)
        self.data_manager.place_repository.get.return_value = place

        result = self.data_manager.get_place(place_id)
        self.data_manager.place_repository.get.assert_called_once_with(place_id)
        self.assertEqual(result, place)

    # Tests for User
    def test_save_user(self):
        user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'hashed_password': 'password123'
        }
        user_id = 'user_123'
        self.data_manager.user_repository.save.return_value = user_id

        result = self.data_manager.save_user(user_data)
        self.data_manager.user_repository.save.assert_called_once()
        self.assertEqual(result, user_id)

    def test_get_user(self):
        user_id = 'user_123'
        user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'hashed_password': 'password123'
        }
        user = User(user_id=user_id, **user_data)
        self.data_manager.user_repository.get.return_value = user

        result = self.data_manager.get_user(user_id)
        self.data_manager.user_repository.get.assert_called_once_with(user_id)
        self.assertEqual(result, user)

    # Tests for Review
    def test_save_review(self):
        review_data = {
            'comment': 'Great place!',
            'user_id': 'user_123',
            'place_id': 'place_123',
            'rating': 5
        }
        review_id = 'review_123'
        self.data_manager.review_repository.save.return_value = review_id

        result = self.data_manager.save_review(review_data)
        self.data_manager.review_repository.save.assert_called_once()
        self.assertEqual(result, review_id)

    def test_get_review(self):
        review_id = 'review_123'
        review_data = {
            'comment': 'Great place!',
            'user_id': 'user_123',
            'place_id': 'place_123',
            'rating': 5
        }
        review = Review(review_id=review_id, **review_data)
        self.data_manager.review_repository.get.return_value = review

        result = self.data_manager.get_review(review_id)
        self.data_manager.review_repository.get.assert_called_once_with(review_id)
        self.assertEqual(result, review)

    # Tests for Amenity
    def test_save_amenity(self):
        amenity_data = {'name': 'Test Amenity'}
        amenity_id = str(uuid4())
        self.data_manager.amenity_repository.save.return_value = amenity_id

        result = self.data_manager.save_amenity(amenity_data)
        self.data_manager.amenity_repository.save.assert_called_once()
        self.assertEqual(result, amenity_id)

    def test_get_amenity(self):
        amenity_id = 'amenity_123'
        amenity_data = {'name': 'Test Amenity'}
        amenity = Amenity(amenity_id=amenity_id, **amenity_data)
        self.data_manager.amenity_repository.get.return_value = amenity

        result = self.data_manager.get_amenity(amenity_id)
        self.data_manager.amenity_repository.get.assert_called_once_with(amenity_id)
        self.assertEqual(result, amenity)

    # Tests for Country
    def test_save_country(self):
        country_data = {'name': 'Test Country'}
        country_id = str(uuid4())
        self.data_manager.country_repository.save.return_value = country_id

        result = self.data_manager.save_country(country_data)
        self.data_manager.country_repository.save.assert_called_once()
        self.assertEqual(result, country_id)

    def test_get_country(self):
        country_id = 'country_123'
        country_data = {'name': 'Test Country'}
        country = Country(country_id=country_id, **country_data)
        self.data_manager.country_repository.get.return_value = country

        result = self.data_manager.get_country(country_id)
        self.data_manager.country_repository.get.assert_called_once_with(country_id)
        self.assertEqual(result, country)

    # Tests for City
    def test_save_city(self):
        city_data = {
            'name': 'Test City',
            'country_id': 'country_123'
        }
        city_id = str(uuid4())
        self.data_manager.city_repository.save.return_value = city_id

        result = self.data_manager.save_city(city_data)
        self.data_manager.city_repository.save.assert_called_once()
        self.assertEqual(result, city_id)

    def test_get_city(self):
        city_id = 'city_123'
        city_data = {
            'name': 'Test City',
            'country_id': 'country_123'
        }
        city = City(city_id=city_id, **city_data)
        self.data_manager.city_repository.get.return_value = city

        result = self.data_manager.get_city(city_id)
        self.data_manager.city_repository.get.assert_called_once_with(city_id)
        self.assertEqual(result, city)

if __name__ == '__main__':
    unittest.main()
