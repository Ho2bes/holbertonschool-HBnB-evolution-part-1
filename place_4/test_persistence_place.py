import unittest
from model_place import Place
from persistence_place import PlaceRepository, PlaceDataManager

class PlaceRepositoryTestCase(unittest.TestCase):
    def setUp(self):
        self.repo = PlaceRepository()
        self.data_manager = PlaceDataManager(self.repo)
        self.place_data = {
            "name": "Test Place",
            "description": "A place for testing",
            "address": "123 Test St",
            "city_id": 1,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "host_id": 1,
            "number_of_rooms": 2,
            "number_of_bathrooms": 1,
            "price_per_night": 100.0,
            "max_guests": 4,
            "amenity_ids": ["wifi", "pool"]
        }

    def test_create_place(self):
        place_id = self.data_manager.create_place(self.place_data)
        self.assertIsNotNone(self.repo.get(place_id))
        self.assertEqual(self.repo.get(place_id).name, "Test Place")

    def test_get_place(self):
        place_id = self.data_manager.create_place(self.place_data)
        place = self.data_manager.get_place(place_id)
        self.assertEqual(place.name, "Test Place")

    def test_update_place(self):
        place_id = self.data_manager.create_place(self.place_data)
        new_data = {"name": "Updated Place"}
        self.assertTrue(self.data_manager.update_place(place_id, new_data))
        self.assertEqual(self.repo.get(place_id).name, "Updated Place")

    def test_delete_place(self):
        place_id = self.data_manager.create_place(self.place_data)
        self.assertTrue(self.data_manager.delete_place(place_id))
        self.assertIsNone(self.repo.get(place_id))

    def test_get_all_places(self):
        self.data_manager.create_place(self.place_data)
        all_places = self.data_manager.get_all_places()
        self.assertEqual(len(all_places), 1)

if __name__ == '__main__':
    unittest.main()

