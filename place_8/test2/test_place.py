# test2/test_place.py

import unittest
import sys
import os

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.place import Place

class TestPlace(unittest.TestCase):

    def test_place_creation(self):
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
        self.assertEqual(place.name, 'Test Place')
        self.assertIsNotNone(place.place_id)
        self.assertIsNotNone(place.created_at)
        self.assertIsNotNone(place.updated_at)

    def test_to_dict(self):
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
        place_dict = place.to_dict()
        self.assertEqual(place_dict['name'], 'Test Place')
        self.assertEqual(place_dict['place_id'], place.place_id)

if __name__ == '__main__':
    unittest.main()
