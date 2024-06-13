# test2/test_data_manager.py

import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_manager import DataManager
from model.place import Place
from model.user import User
from model.review import Review
from model.amenity import Amenity
from model.country import Country
from model.city import City

class TestDataManager(unittest.TestCase):

    def setUp(self):
        self.data_manager = DataManager()

    def test_save_place(self):
        place_data = {
            'name': 'Test Place',
            'description': 'A place for testing',
            'address': '123 Test St',
            'city_id': '1',
            'latitude': 40.7128,
            'longitude': -74.0060,
            'host_id': '1',
            'number_of_rooms': 3,
            'number_of_bathrooms': 2,
            'price_per_night': 100.0,
            'max_guests': 4,
            'amenity_ids': ['1', '2']
        }
        place_id = self.data_manager.save_place(place_data)
        self.assertIsNotNone(place_id)
        place = self.data_manager.get_place(place_id)
        self.assertEqual(place.name, 'Test Place')

    def test_update_place(self):
        place_data = {
            'name': 'Test Place',
            'description': 'A place for testing',
            'address': '123 Test St',
            'city_id': '1',
            'latitude': 40.7128,
            'longitude': -74.0060,
            'host_id': '1',
            'number_of_rooms': 3,
            'number_of_bathrooms': 2,
            'price_per_night': 100.0,
            'max_guests': 4,
            'amenity_ids': ['1', '2']
        }
        place_id = self.data_manager.save_place(place_data)
        new_data = {'name': 'Updated Place'}
        self.data_manager.update_place(place_id, new_data)
        place = self.data_manager.get_place(place_id)
        self.assertEqual(place.name, 'Updated Place')

    def test_delete_place(self):
        place_data = {
            'name': 'Test Place',
            'description': 'A place for testing',
            'address': '123 Test St',
            'city_id': '1',
            'latitude': 40.7128,
            'longitude': -74.0060,
            'host_id': '1',
            'number_of_rooms': 3,
            'number_of_bathrooms': 2,
            'price_per_night': 100.0,
            'max_guests': 4,
            'amenity_ids': ['1', '2']
        }
        place_id = self.data_manager.save_place(place_data)
        self.data_manager.delete_place(place_id)
        place = self.data_manager.get_place(place_id)
        self.assertIsNone(place)

    def test_save_user(self):
        user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password'
        }
        user_id = self.data_manager.save_user(user_data)
        self.assertIsNotNone(user_id)
        user = self.data_manager.get_user(user_id)
        self.assertEqual(user.username, 'testuser')

    def test_update_user(self):
        user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password'
        }
        user_id = self.data_manager.save_user(user_data)
        new_data = {'username': 'updateduser'}
        self.data_manager.update_user(user_id, new_data)
        user = self.data_manager.get_user(user_id)
        self.assertEqual(user.username, 'updateduser')

    def test_delete_user(self):
        user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password'
        }
        user_id = self.data_manager.save_user(user_data)
        self.data_manager.delete_user(user_id)
        user = self.data_manager.get_user(user_id)
        self.assertIsNone(user)

    def test_save_review(self):
        review_data = {
            'user_id': '1',
            'place_id': '1',
            'rating': 5,
            'comment': 'Great place!'
        }
        review_id = self.data_manager.save_review(review_data)
        self.assertIsNotNone(review_id)
        review = self.data_manager.get_review(review_id)
        self.assertEqual(review.comment, 'Great place!')

    def test_update_review(self):
        review_data = {
            'user_id': '1',
            'place_id': '1',
            'rating': 5,
            'comment': 'Great place!'
        }
        review_id = self.data_manager.save_review(review_data)
        new_data = {'comment': 'Updated comment'}
        self.data_manager.update_review(review_id, new_data)
        review = self.data_manager.get_review(review_id)
        self.assertEqual(review.comment, 'Updated comment')

    def test_delete_review(self):
        review_data = {
            'user_id': '1',
            'place_id': '1',
            'rating': 5,
            'comment': 'Great place!'
        }
        review_id = self.data_manager.save_review(review_data)
        self.data_manager.delete_review(review_id)
        review = self.data_manager.get_review(review_id)
        self.assertIsNone(review)

    def test_save_amenity(self):
        amenity_data = {'name': 'WiFi'}
        amenity_id = self.data_manager.save_amenity(amenity_data)
        self.assertIsNotNone(amenity_id)
        amenity = self.data_manager.get_amenity(amenity_id)
        self.assertEqual(amenity.name, 'WiFi')

    def test_update_amenity(self):
        amenity_data = {'name': 'WiFi'}
        amenity_id = self.data_manager.save_amenity(amenity_data)
        new_data = {'name': 'Updated WiFi'}
        self.data_manager.update_amenity(amenity_id, new_data)
        amenity = self.data_manager.get_amenity(amenity_id)
        self.assertEqual(amenity.name, 'Updated WiFi')

    def test_delete_amenity(self):
        amenity_data = {'name': 'WiFi'}
        amenity_id = self.data_manager.save_amenity(amenity_data)
        self.data_manager.delete_amenity(amenity_id)
        amenity = self.data_manager.get_amenity(amenity_id)
        self.assertIsNone(amenity)

    def test_save_country(self):
        country_data = {'name': 'USA'}
        country_id = self.data_manager.save_country(country_data)
        self.assertIsNotNone(country_id)
        country = self.data_manager.get_country(country_id)
        self.assertEqual(country.name, 'USA')

    def test_update_country(self):
        country_data = {'name': 'USA'}
        country_id = self.data_manager.save_country(country_data)
        new_data = {'name': 'Updated Country'}
        self.data_manager.update_country(country_id, new_data)
        country = self.data_manager.get_country(country_id)
        self.assertEqual(country.name, 'Updated Country')

    def test_delete_country(self):
        country_data = {'name': 'USA'}
        country_id = self.data_manager.save_country(country_data)
        self.data_manager.delete_country(country_id)
        country = self.data_manager.get_country(country_id)
        self.assertIsNone(country)

    def test_save_city(self):
        city_data = {'name': 'New York', 'country_id': '1'}
        city_id = self.data_manager.save_city(city_data)
        self.assertIsNotNone(city_id)
        city = self.data_manager.get_city(city_id)
        self.assertEqual(city.name, 'New York')

    def test_update_city(self):
        city_data = {'name': 'New York', 'country_id': '1'}
        city_id = self.data_manager.save_city(city_data)
        new_data = {'name': 'Updated City'}
        self.data_manager.update_city(city_id, new_data)
        city = self.data_manager.get_city(city_id)
        self.assertEqual(city.name, 'Updated City')

    def test_delete_city(self):
        city_data = {'name': 'New York', 'country_id': '1'}
        city_id = self.data_manager.save_city(city_data)
        self.data_manager.delete_city(city_id)
        city = self.data_manager.get_city(city_id)
        self.assertIsNone(city)

if __name__ == '__main__':
    unittest.main()
