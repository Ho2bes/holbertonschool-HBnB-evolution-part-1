import unittest
from model.place import Place
from persistence.data_manager import PlaceRepository

class TestPlaceModel(unittest.TestCase):

    def setUp(self):
        self.place_repo = PlaceRepository()
        self.place_data = {
            'name': 'Test Place',
            'description': 'A place for testing',
            'address': '123 Test St',
            'city_id': 1,
            'latitude': 48.8566,
            'longitude': 2.3522,
            'host_id': 1,
            'number_of_rooms': 3,
            'number_of_bathrooms': 2,
            'price_per_night': 100.0,
            'max_guests': 4,
            'amenity_ids': []
        }

    def test_create_place(self):
        place_id = self.place_repo.create_place(self.place_data)
        place = self.place_repo.get(place_id)
        self.assertEqual(place.name, self.place_data['name'])
        self.assertEqual(place.description, self.place_data['description'])

    def test_update_place(self):
        place_id = self.place_repo.create_place(self.place_data)
        new_data = {'name': 'Updated Place'}
        self.place_repo.update(place_id, new_data)
        place = self.place_repo.get(place_id)
        self.assertEqual(place.name, 'Updated Place')

    def test_delete_place(self):
        place_id = self.place_repo.create_place(self.place_data)
        self.place_repo.delete(place_id)
        place = self.place_repo.get(place_id)
        self.assertIsNone(place)

if __name__ == '__main__':
    unittest.main()
