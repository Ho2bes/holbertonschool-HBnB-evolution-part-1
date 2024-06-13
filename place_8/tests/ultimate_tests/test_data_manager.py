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
        place_id = str(uuid4())
        place = Place(**place_data)
        place.place_id = place_id
        self.data_manager.place_repository.save.return_value = place_id

        result = self.data_manager.save_place(place_data)
        self.data_manager.place_repository.save.assert_called_once_with(place)
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
        place = Place(**place_data)
        place.place_id = place_id
        self.data_manager.place_repository.get.return_value = place

        result = self.data_manager.get_place(place_id)
        self.data_manager.place_repository.get.assert_called_once_with(place_id)
        self.assertEqual(result, place)

    def test_update_place(self):
        place_id = 'place_123'
        new_data = {'name': 'Updated Place'}
        self.data_manager.place_repository.update.return_value = True

        result = self.data_manager.update_place(place_id, new_data)
        self.data_manager.place_repository.update.assert_called_once_with(place_id, new_data)
        self.assertTrue(result)

    def test_delete_place(self):
        place_id = 'place_123'
        self.data_manager.place_repository.delete.return_value = True

        result = self.data_manager.delete_place(place_id)
        self.data_manager.place_repository.delete.assert_called_once_with(place_id)
        self.assertTrue(result)

    def test_get_all_places(self):
        places = [Place(
            name='Test Place',
            description='A nice place',
            address='123 Main St',
            city_id='city_123',
            latitude=40.7128,
            longitude=-74.0060,
            host_id='host_123',
            number_of_rooms=3,
            number_of_bathrooms=2,
            price_per_night=150,
            max_guests=4,
            amenity_ids=['amenity_1', 'amenity_2']
        )]
        self.data_manager.place_repository.get_all.return_value = places

        result = self.data_manager.get_all_places()
        self.data_manager.place_repository.get_all.assert_called_once()
        self.assertEqual(result, places)

    # Tests for User
    def test_save_user(self):
        user_data = {
            'user_id': str(uuid4()),
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'hashed_password': 'password123'
        }
        user = User(**user_data)
        self.data_manager.user_repository.save.return_value = user.user_id

        result = self.data_manager.save_user(user_data)
        self.data_manager.user_repository.save.assert_called_once_with(user)
        self.assertEqual(result, user.user_id)

    def test_get_user(self):
        user_id = 'user_123'
        user_data = {
            'user_id': user_id,
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'hashed_password': 'password123'
        }
        user = User(**user_data)
        self.data_manager.user_repository.get.return_value = user

        result = self.data_manager.get_user(user_id)
        self.data_manager.user_repository.get.assert_called_once_with(user_id)
        self.assertEqual(result, user)

    def test_update_user(self):
        user_id = 'user_123'
        new_data = {'first_name': 'Jane'}
        self.data_manager.user_repository.update.return_value = True

        result = self.data_manager.update_user(user_id, new_data)
        self.data_manager.user_repository.update.assert_called_once_with(user_id, new_data)
        self.assertTrue(result)

    def test_delete_user(self):
        user_id = 'user_123'
        self.data_manager.user_repository.delete.return_value = True

        result = self.data_manager.delete_user(user_id)
        self.data_manager.user_repository.delete.assert_called_once_with(user_id)
        self.assertTrue(result)

    def test_get_all_users(self):
        users = [User(
            user_id=str(uuid4()),
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            hashed_password='password123'
        )]
        self.data_manager.user_repository.get_all.return_value = users

        result = self.data_manager.get_all_users()
        self.data_manager.user_repository.get_all.assert_called_once()
        self.assertEqual(result, users)

    # Tests for Review
    def test_save_review(self):
        review_data = {
            'comment': 'Great place!',
            'user_id': 'user_123',
            'place_id': 'place_123',
            'rating': 5
        }
        review_id = str(uuid4())
        review = Review(**review_data)
        review.review_id = review_id
        self.data_manager.review_repository.save.return_value = review_id

        result = self.data_manager.save_review(review_data)
        self.data_manager.review_repository.save.assert_called_once_with(review)
        self.assertEqual(result, review_id)

    def test_get_review(self):
        review_id = 'review_123'
        review_data = {
            'comment': 'Great place!',
            'user_id': 'user_123',
            'place_id': 'place_123',
            'rating': 5
        }
        review = Review(**review_data)
        review.review_id = review_id
        self.data_manager.review_repository.get.return_value = review

        result = self.data_manager.get_review(review_id)
        self.data_manager.review_repository.get.assert_called_once_with(review_id)
        self.assertEqual(result, review)

    def test_update_review(self):
        review_id = 'review_123'
        new_data = {'comment': 'Updated review'}
        self.data_manager.review_repository.update.return_value = True

        result = self.data_manager.update_review(review_id, new_data)
        self.data_manager.review_repository.update.assert_called_once_with(review_id, new_data)
        self.assertTrue(result)

    def test_delete_review(self):
        review_id = 'review_123'
        self.data_manager.review_repository.delete.return_value = True

        result = self.data_manager.delete_review(review_id)
        self.data_manager.review_repository.delete.assert_called_once_with(review_id)
        self.assertTrue(result)

    def test_get_all_reviews(self):
        reviews = [Review(
            comment='Great place!',
            user_id='user_123',
            place_id='place_123',
            rating=5
        )]
        self.data_manager.review_repository.get_all.return_value = reviews

        result = self.data_manager.get_all_reviews()
        self.data_manager.review_repository.get_all.assert_called_once()
        self.assertEqual(result, reviews)

    # Tests for Amenity
    def test_save_amenity(self):
        amenity_data = {'name': 'Test Amenity'}
        amenity_id = str(uuid4())
        amenity = Amenity(**amenity_data)
        amenity.amenity_id = amenity_id
        self.data_manager.amenity_repository.save.return_value = amenity_id

        result = self.data_manager.save_amenity(amenity_data)
        self.data_manager.amenity_repository.save.assert_called_once_with(amenity)
        self.assertEqual(result, amenity_id)

    def test_get_amenity(self):
        amenity_id = 'amenity_123'
        amenity_data = {'name': 'Test Amenity'}
        amenity = Amenity(**amenity_data)
        amenity.amenity_id = amenity_id
        self.data_manager.amenity_repository.get.return_value = amenity

        result = self.data_manager.get_amenity(amenity_id)
        self.data_manager.amenity_repository.get.assert_called_once_with(amenity_id)
        self.assertEqual(result, amenity)

    def test_update_amenity(self):
        amenity_id = 'amenity_123'
        new_data = {'name': 'Updated Amenity'}
        self.data_manager.amenity_repository.update.return_value = True

        result = self.data_manager.update_amenity(amenity_id, new_data)
        self.data_manager.amenity_repository.update.assert_called_once_with(amenity_id, new_data)
        self.assertTrue(result)

    def test_delete_amenity(self):
        amenity_id = 'amenity_123'
        self.data_manager.amenity_repository.delete.return_value = True

        result = self.data_manager.delete_amenity(amenity_id)
        self.data_manager.amenity_repository.delete.assert_called_once_with(amenity_id)
        self.assertTrue(result)

    def test_get_all_amenities(self):
        amenities = [Amenity(name='Test Amenity')]
        self.data_manager.amenity_repository.get_all.return_value = amenities

        result = self.data_manager.get_all_amenities()
        self.data_manager.amenity_repository.get_all.assert_called_once()
        self.assertEqual(result, amenities)

    # Tests for Country
    def test_save_country(self):
        country_data = {'name': 'Test Country'}
        country_id = str(uuid4())
        country = Country(**country_data)
        country.country_id = country_id
        self.data_manager.country_repository.save.return_value = country_id

        result = self.data_manager.save_country(country_data)
        self.data_manager.country_repository.save.assert_called_once_with(country)
        self.assertEqual(result, country_id)

    def test_get_country(self):
        country_id = 'country_123'
        country_data = {'name': 'Test Country'}
        country = Country(**country_data)
        country.country_id = country_id
        self.data_manager.country_repository.get.return_value = country

        result = self.data_manager.get_country(country_id)
        self.data_manager.country_repository.get.assert_called_once_with(country_id)
        self.assertEqual(result, country)

    def test_update_country(self):
        country_id = 'country_123'
        new_data = {'name': 'Updated Country'}
        self.data_manager.country_repository.update.return_value = True

        result = self.data_manager.update_country(country_id, new_data)
        self.data_manager.country_repository.update.assert_called_once_with(country_id, new_data)
        self.assertTrue(result)

    def test_delete_country(self):
        country_id = 'country_123'
        self.data_manager.country_repository.delete.return_value = True

        result = self.data_manager.delete_country(country_id)
        self.data_manager.country_repository.delete.assert_called_once_with(country_id)
        self.assertTrue(result)

    def test_get_all_countries(self):
        countries = [Country(name='Test Country')]
        self.data_manager.country_repository.get_all.return_value = countries

        result = self.data_manager.get_all_countries()
        self.data_manager.country_repository.get_all.assert_called_once()
        self.assertEqual(result, countries)

    # Tests for City
    def test_save_city(self):
        city_data = {'name': 'Test City', 'country_id': 'country_123'}
        city_id = str(uuid4())
        city = City(**city_data)
        city.city_id = city_id
        self.data_manager.city_repository.save.return_value = city_id

        result = self.data_manager.save_city(city_data)
        self.data_manager.city_repository.save.assert_called_once_with(city)
        self.assertEqual(result, city_id)

    def test_get_city(self):
        city_id = 'city_123'
        city_data = {'name': 'Test City', 'country_id': 'country_123'}
        city = City(**city_data)
        city.city_id = city_id
        self.data_manager.city_repository.get.return_value = city

        result = self.data_manager.get_city(city_id)
        self.data_manager.city_repository.get.assert_called_once_with(city_id)
        self.assertEqual(result, city)

    def test_update_city(self):
        city_id = 'city_123'
        new_data = {'name': 'Updated City'}
        self.data_manager.city_repository.update.return_value = True

        result = self.data_manager.update_city(city_id, new_data)
        self.data_manager.city_repository.update.assert_called_once_with(city_id, new_data)
        self.assertTrue(result)

    def test_delete_city(self):
        city_id = 'city_123'
        self.data_manager.city_repository.delete.return_value = True

        result = self.data_manager.delete_city(city_id)
        self.data_manager.city_repository.delete.assert_called_once_with(city_id)
        self.assertTrue(result)

    def test_get_all_cities(self):
        cities = [City(name='Test City', country_id='country_123')]
        self.data_manager.city_repository.get_all.return_value = cities

        result = self.data_manager.get_all_cities()
        self.data_manager.city_repository.get_all.assert_called_once()
        self.assertEqual(result, cities)

if __name__ == '__main__':
    unittest.main()
