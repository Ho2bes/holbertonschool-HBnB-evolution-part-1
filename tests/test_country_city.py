import unittest
from model.city import City
from persistence.data_manager import CityRepository

class TestCityModel(unittest.TestCase):

    def setUp(self):
        self.city_repo = CityRepository()
        self.city_data = {
            'name': 'Paris',
            'country_code': 'FR'
        }

    def test_create_city(self):
        city = City(self.city_data['name'], self.city_data['country_code'])
        self.city_repo.save(city)
        saved_city = self.city_repo.get(city.city_id)
        self.assertEqual(saved_city.name, self.city_data['name'])

    def test_update_city(self):
        city = City(self.city_data['name'], self.city_data['country_code'])
        self.city_repo.save(city)
        new_data = {'name': 'Updated Paris'}
        self.city_repo.update(city.city_id, new_data)
        updated_city = self.city_repo.get(city.city_id)
        self.assertEqual(updated_city.name, 'Updated Paris')

    def test_delete_city(self):
        city = City(self.city_data['name'], self.city_data['country_code'])
        self.city_repo.save(city)
        self.city_repo.delete(city.city_id)
        deleted_city = self.city_repo.get(city.city_id)
        self.assertIsNone(deleted_city)

if __name__ == '__main__':
    unittest.main()
