import unittest
import os
import sys
import uuid

# Ajouter le répertoire parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

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
        self.place_data = {
            'name': 'Test Place',
            'description': 'A place for testing',
            'address': '123 Test St',
            'city_id': str(uuid.uuid4()),
            'latitude': 40.7128,
            'longitude': -74.0060,
            'host_id': str(uuid.uuid4()),
            'number_of_rooms': 3,
            'number_of_bathrooms': 2,
            'price_per_night': 150.0,
            'max_guests': 4,
            'amenity_ids': [str(uuid.uuid4()), str(uuid.uuid4())]
        }
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123'
        }
        self.review_data = {
            'user_id': str(uuid.uuid4()),
            'place_id': str(uuid.uuid4()),
            'rating': 5,
            'comment': 'Great place!'
        }
        self.amenity_data = {
            'name': 'WiFi'
        }
        self.country_data = {
            'name': 'Test Country'
        }
        self.city_data = {
            'name': 'Test City',
            'country_id': str(uuid.uuid4())
        }

    def test_save_place(self):
        place_id = self.data_manager.save_place(self.place_data)
        self.assertIsNotNone(place_id)

    def test_get_place(self):
        place_id = self.data_manager.save_place(self.place_data)
        place = self.data_manager.get_place(place_id)
        self.assertEqual(place.place_id, place_id)

    def test_update_place(self):
        place_id = self.data_manager.save_place(self.place_data)
        updated_data = {'name': 'Updated Place'}
        self.data_manager.update_place(place_id, updated_data)
        updated_place = self.data_manager.get_place(place_id)
        self.assertEqual(updated_place.name, 'Updated Place')

    def test_delete_place(self):
        place_id = self.data_manager.save_place(self.place_data)
        self.data_manager.delete_place(place_id)
        place = self.data_manager.get_place(place_id)
        self.assertIsNone(place)

    def test_save_user(self):
        user_id = self.data_manager.save_user(self.user_data)
        self.assertIsNotNone(user_id)

    def test_get_user(self):
        user_id = self.data_manager.save_user(self.user_data)
        user = self.data_manager.get_user(user_id)
        self.assertEqual(user.user_id, user_id)

    def test_update_user(self):
        user_id = self.data_manager.save_user(self.user_data)
        updated_data = {'username': 'updateduser'}
        self.data_manager.update_user(user_id, updated_data)
        updated_user = self.data_manager.get_user(user_id)
        self.assertEqual(updated_user.username, 'updateduser')

    def test_delete_user(self):
        user_id = self.data_manager.save_user(self.user_data)
        self.data_manager.delete_user(user_id)
        user = self.data_manager.get_user(user_id)
        self.assertIsNone(user)

    def test_save_review(self):
        review_id = self.data_manager.save_review(self.review_data)
        self.assertIsNotNone(review_id)

    def test_get_review(self):
        review_id = self.data_manager.save_review(self.review_data)
        review = self.data_manager.get_review(review_id)
        self.assertEqual(review.review_id, review_id)

    def test_update_review(self):
        review_id = self.data_manager.save_review(self.review_data)
        updated_data = {'comment': 'Updated comment'}
        self.data_manager.update_review(review_id, updated_data)
        updated_review = self.data_manager.get_review(review_id)
        self.assertEqual(updated_review.comment, 'Updated comment')

    def test_delete_review(self):
        review_id = self.data_manager.save_review(self.review_data)
        self.data_manager.delete_review(review_id)
        review = self.data_manager.get_review(review_id)
        self.assertIsNone(review)

    def test_save_amenity(self):
        amenity_id = self.data_manager.save_amenity(self.amenity_data)
        self.assertIsNotNone(amenity_id)

    def test_get_amenity(self):
        amenity_id = self.data_manager.save_amenity(self.amenity_data)
        amenity = self.data_manager.get_amenity(amenity_id)
        self.assertEqual(amenity.amenity_id, amenity_id)

    def test_update_amenity(self):
        amenity_id = self.data_manager.save_amenity(self.amenity_data)
        updated_data = {'name': 'Updated WiFi'}
        self.data_manager.update_amenity(amenity_id, updated_data)
        updated_amenity = self.data_manager.get_amenity(amenity_id)
        self.assertEqual(updated_amenity.name, 'Updated WiFi')

    def test_delete_amenity(self):
        amenity_id = self.data_manager.save_amenity(self.amenity_data)
        self.data_manager.delete_amenity(amenity_id)
        amenity = self.data_manager.get_amenity(amenity_id)
        self.assertIsNone(amenity)

    def test_save_country(self):
        country_id = self.data_manager.save_country(self.country_data)
        self.assertIsNotNone(country_id)

    def test_get_country(self):
        country_id = self.data_manager.save_country(self.country_data)
        country = self.data_manager.get_country(country_id)
        self.assertEqual(country.country_id, country_id)

    def test_update_country(self):
        country_id = self.data_manager.save_country(self.country_data)
        updated_data = {'name': 'Updated Country'}
        self.data_manager.update_country(country_id, updated_data)
        updated_country = self.data_manager.get_country(country_id)
        self.assertEqual(updated_country.name, 'Updated Country')

    def test_delete_country(self):
        country_id = self.data_manager.save_country(self.country_data)
        self.data_manager.delete_country(country_id)
        country = self.data_manager.get_country(country_id)
        self.assertIsNone(country)

    def test_save_city(self):
        city_id = self.data_manager.save_city(self.city_data)
        self.assertIsNotNone(city_id)

    def test_get_city(self):
        city_id = self.data_manager.save_city(self.city_data)
        city = self.data_manager.get_city(city_id)
        self.assertEqual(city.city_id, city_id)

    def test_update_city(self):
        city_id = self.data_manager.save_city(self.city_data)
        updated_data = {'name': 'Updated City'}
        self.data_manager.update_city(city_id, updated_data)
        updated_city = self.data_manager.get_city(city_id)
        self.assertEqual(updated_city.name, 'Updated City')

    def test_delete_city(self):
        city_id = self.data_manager.save_city(self.city_data)
        self.data_manager.delete_city(city_id)
        city = self.data_manager.get_city(city_id)
        self.assertIsNone(city)

if __name__ == '__main__':
    unittest.main()
