# test2/test_place_repository.py

import unittest
import sys
import os

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.place import Place
from persistence.place_repository import PlaceRepository

class TestPlaceRepository(unittest.TestCase):

    def setUp(self):
        self.repo = PlaceRepository()

    def test_save_place(self):
        place = Place(
            name='Test Place',
            description='A place for testing',
            address='123 Test St',
            city_id='1',
            latitude=40.7128,
            longitude=-74.0060,
            host_id='1',
            number_of_rooms=3,
            number_of_bathrooms=2,
            price_per_night=100.0,
            max_guests=4,
            amenity_ids=['1', '2']
        )
        self.repo.save(place)
        self.assertIn(place.place_id, self.repo.places)

    def test_get_place(self):
        place = Place(
            name='Test Place',
            description='A place for testing',
            address='123 Test St',
            city_id='1',
            latitude=40.7128,
            longitude=-74.0060,
            host_id='1',
            number_of_rooms=3,
            number_of_bathrooms=2,
            price_per_night=100.0,
            max_guests=4,
            amenity_ids=['1', '2']
        )
        self.repo.save(place)
        fetched = self.repo.get(place.place_id)
        self.assertEqual(fetched.name, 'Test Place')

    def test_update_place(self):
        place = Place(
            name='Test Place',
            description='A place for testing',
            address='123 Test St',
            city_id='1',
            latitude=40.7128,
            longitude=-74.0060,
            host_id='1',
            number_of_rooms=3,
            number_of_bathrooms=2,
            price_per_night=100.0,
            max_guests=4,
            amenity_ids=['1', '2']
        )
        self.repo.save(place)
        update_data = {'name': 'Updated Place'}
        self.repo.update(place.place_id, update_data)
        updated = self.repo.get(place.place_id)
        self.assertEqual(updated.name, 'Updated Place')

    def test_delete_place(self):
        place = Place(
            name='Test Place',
            description='A place for testing',
            address='123 Test St',
            city_id='1',
            latitude=40.7128,
            longitude=-74.0060,
            host_id='1',
            number_of_rooms=3,
            number_of_bathrooms=2,
            price_per_night=100.0,
            max_guests=4,
            amenity_ids=['1', '2']
        )
        self.repo.save(place)
        self.repo.delete(place.place_id)
        self.assertIsNone(self.repo.get(place.place_id))

if __name__ == '__main__':
    unittest.main()
