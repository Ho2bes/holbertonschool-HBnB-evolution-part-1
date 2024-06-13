# test2/test_country_repository.py

import unittest
import sys
import os

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.country import Country
from persistence.country_repository import CountryRepository

class TestCountryRepository(unittest.TestCase):

    def setUp(self):
        self.repo = CountryRepository()

    def test_save_country(self):
        country = Country(name='USA')
        self.repo.save(country)
        self.assertIn(country.country_id, self.repo.countries)

    def test_get_country(self):
        country = Country(name='USA')
        self.repo.save(country)
        fetched = self.repo.get(country.country_id)
        self.assertEqual(fetched.name, 'USA')

    def test_update_country(self):
        country = Country(name='USA')
        self.repo.save(country)
        update_data = {'name': 'Updated Country'}
        self.repo.update(country.country_id, update_data)
        updated = self.repo.get(country.country_id)
        self.assertEqual(updated.name, 'Updated Country')

    def test_delete_country(self):
        country = Country(name='USA')
        self.repo.save(country)
        self.repo.delete(country.country_id)
        self.assertIsNone(self.repo.get(country.country_id))

if __name__ == '__main__':
    unittest.main()
