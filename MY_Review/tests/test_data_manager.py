
Copier le code
#!/usr/bin/python3
import unittest
from unittest.mock import MagicMock
from place_7.data_manager import DataManager
from place_7.model.place import Place
from place_7.model.user import User
from place_7.model.review import Review
from place_7.model.amenity import Amenity
from place_7.model.country import Country
from place_7.model.city import City

class TestDataManager(unittest.TestCase):

    def setUp(self):
        self.data_manager = DataManager()

        # Mock repositories
        self.data_manager.place_repository = MagicMock()
        self.data_manager.user_repository = MagicMock()
        self.data_manager.review_repository = MagicMock()
        self.data_manager.amenity_repository = MagicMock()
        self.data_manager.country_repository = MagicMock()
        self.data_manager.city_repository = MagicMock()

    # Tests for Place methods
    def test_save_place(self):
        place_data = {'name': 'Test Place', 'location': 'Test Location'}
        self.data_manager.save_place(place_data)
        self.data_manager.place_repository.save.assert_called_once()

    def test_get_place(self):
        place_id = 1
        self.data_manager.get_place(place_id)
        self.data_manager.place_repository.get.assert_called_once_with(place_id)

    def test_update_place(self):
        place_id = 1
        new_data = {'name': 'Updated Place'}
        self.data_manager.update_place(place_id, new_data)
        self.data_manager.place_repository.update.assert_called_once_with(place_id, new_data)

    def test_delete_place(self):
        place_id = 1
        self.data_manager.delete_place(place_id)
        self.data_manager.place_repository.delete.assert_called_once_with(place_id)

    def test_get_all_places(self):
        self.data_manager.get_all_places()
        self.data_manager.place_repository.get_all.assert_called_once()

    # Tests for User methods
    def test_save_user(self):
        user_data = {'name': 'Test User', 'email': 'test@example.com'}
        self.data_manager.save_user(user_data)
        self.data_manager.user_repository.save.assert_called_once()

    def test_get_user(self):
        user_id = 1
        self.data_manager.get_user(user_id)
        self.data_manager.user_repository.get.assert_called_once_with(user_id)

    def test_update_user(self):
        user_id = 1
        new_data = {'name': 'Updated User'}
        self.data_manager.update_user(user_id, new_data)
        self.data_manager.user_repository.update.assert_called_once_with(user_id, new_data)

    def test_delete_user(self):
        user_id = 1
        self.data_manager.delete_user(user_id)
        self.data_manager.user_repository.delete.assert_called_once_with(user_id)

    def test_get_all_users(self):
        self.data_manager.get_all_users()
        self.data_manager.user_repository.get_all.assert_called_once()

    # Tests for Review methods
    def test_save_review(self):
        review_data = {'text': 'Great product', 'rating': 5}
        self.data_manager.save_review(review_data)
        self.data_manager.review_repository.save.assert_called_once()

    def test_get_review(self):
        review_id = 1
        self.data_manager.get_review(review_id)
        self.data_manager.review_repository.get.assert_called_once_with(review_id)

    def test_update_review(self):
        review_id = 1
        new_data = {'text': 'Updated review'}
        self.data_manager.update_review(review_id, new_data)
        self.data_manager.review_repository.update.assert_called_once_with(review_id, new_data)

    def test_delete_review(self):
        review_id = 1
        self.data_manager.delete_review(review_id)
        self.data_manager.review_repository.delete.assert_called_once_with(review_id)

    def test_get_all_reviews(self):
        self.data_manager.get_all_reviews()
        self.data_manager.review_repository.get_all.assert_called_once()

    # Tests for Amenity methods
    def test_save_amenity(self):
        amenity_data = {'name': 'WiFi'}
        self.data_manager.save_amenity(amenity_data)
        self.data_manager.amenity_repository.save.assert_called_once()

    def test_get_amenity(self):
        amenity_id = 1
        self.data_manager.get_amenity(amenity_id)
        self.data_manager.amenity_repository.get.assert_called_once_with(amenity_id)

    def test_update_amenity(self):
        amenity_id = 1
        new_data = {'name': 'Updated Amenity'}
        self.data_manager.update_amenity(amenity_id, new_data)
        self.data_manager.amenity_repository.update.assert_called_once_with(amenity_id, new_data)

    def test_delete_amenity(self):
        amenity_id = 1
        self.data_manager.delete_amenity(amenity_id)
        self.data_manager.amenity_repository.delete.assert_called_once_with(amenity_id)

    def test_get_all_amenities(self):
        self.data_manager.get_all_amenities()
        self.data_manager.amenity_repository.get_all.assert_called_once()

    # Tests for Country methods
    def test_save_country(self):
        country_data = {'name': 'Test Country'}
        self.data_manager.save_country(country_data)
        self.data_manager.country_repository.save.assert_called_once()

    def test_get_country(self):
        country_id = 1
        self.data_manager.get_country(country_id)
        self.data_manager.country_repository.get.assert_called_once_with(country_id)

    def test_update_country(self):
        country_id = 1
        new_data = {'name': 'Updated Country'}
        self.data_manager.update_country(country_id, new_data)
        self.data_manager.country_repository.update.assert_called_once_with(country_id, new_data)

    def test_delete_country(self):
        country_id = 1
        self.data_manager.delete_country(country_id)
        self.data_manager.country_repository.delete.assert_called_once_with(country_id)

    def test_get_all_countries(self):
        self.data_manager.get_all_countries()
        self.data_manager.country_repository.get_all.assert_called_once()

    # Tests for City methods
    def test_save_city(self):
        city_data = {'name': 'Test City'}
        self.data_manager.save_city(city_data)
        self.data_manager.city_repository.save.assert_called_once()

    def test_get_city(self):
        city_id = 1
        self.data_manager.get_city(city_id)
        self.data_manager.city_repository.get.assert_called_once_with(city_id)

    def test_update_city(self):
        city_id = 1
        new_data = {'name': 'Updated City'}
        self.data_manager.update_city(city_id, new_data)
        self.data_manager.city_repository.update.assert_called_once_with(city_id, new_data)

    def test_delete_city(self):
        city_id = 1
        self.data_manager.delete_city(city_id)
        self.data_manager.city_repository.delete.assert_called_once_with(city_id)

    def test_get_all_cities(self):
        self.data_manager.get_all_cities()
        self.data_manager.city_repository.get_all.assert_called_once()

if __name__ == '__main__':
    unittest.main()
