# test2/test_city_repository.py

import unittest
import sys
import os

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.city import City
from persistence.city_repository import CityRepository

class TestCityRepository(unittest.TestCase):

    def setUp(self):
        self.repo = CityRepository()

    def test_save_city(self):
        city = City(name='New York', country_id='1')
        self.repo.save(city)
        self.assertIn(city.city_id, self.repo.cities)

    def test_get_city(self):
        city = City(name='New York', country_id='1')
        self.repo.save(city)
        fetched = self.repo.get(city.city_id)
        self.assertEqual(fetched.name, 'New York')

    def test_update_city(self):
        city = City(name='New York', country_id='1')
        self.repo.save(city)
        update_data = {'name': 'Updated City'}
        self.repo.update(city.city_id, update_data)
        updated = self.repo.get(city.city_id)
        self.assertEqual(updated.name, 'Updated City')

    def test_delete_city(self):
        city = City(name='New York', country_id='1')
        self.repo.save(city)
        self.repo.delete(city.city_id)
        self.assertIsNone(self.repo.get(city.city_id))

if __name__ == '__main__':
    unittest.main()
