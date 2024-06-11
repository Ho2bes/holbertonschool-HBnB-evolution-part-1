#!/usr/bin/python3


import unittest
from unittest.mock import MagicMock
from persistence_place import PlaceDataManager, PlaceRepository
from model_place import Place

class TestPlaceDataManager(unittest.TestCase):
    def setUp(self):
        self.repository = PlaceRepository()
        self.data_manager = PlaceDataManager(self.repository)

    def test_save_place(self):
        place = Place(name="Test Place", description="A nice place", address="123 Street", city_id=1,
                      latitude=45.0, longitude=-75.0, host_id=1, number_of_rooms=3, number_of_bathrooms=2,
                      price_per_night=100.0, max_guests=4, amenity_ids=["1", "2"])
        self.data_manager.save(place)
        self.assertEqual(self.repository.get(place.place_id), place)

    def test_get_place(self):
        place = Place(name="Test Place", description="A nice place", address="123 Street", city_id=1,
                      latitude=45.0, longitude=-75.0, host_id=1, number_of_rooms=3, number_of_bathrooms=2,
                      price_per_night=100.0, max_guests=4, amenity_ids=["1", "2"])
        self.data_manager.save(place)
        retrieved_place = self.data_manager.get(place.place_id)
        self.assertEqual(retrieved_place, place)

    def test_update_place(self):
        place = Place(name="Test Place", description="A nice place", address="123 Street", city_id=1,
                      latitude=45.0, longitude=-75.0, host_id=1, number_of_rooms=3, number_of_bathrooms=2,
                      price_per_night=100.0, max_guests=4, amenity_ids=["1", "2"])
        self.data_manager.save(place)
        new_data = {"name": "Updated Place"}
        updated = self.data_manager.update(place.place_id, new_data)
        self.assertTrue(updated)
        self.assertEqual(self.repository.get(place.place_id).name, "Updated Place")

    def test_delete_place(self):
        place = Place(name="Test Place", description="A nice place", address="123 Street", city_id=1,
                      latitude=45.0, longitude=-75.0, host_id=1, number_of_rooms=3, number_of_bathrooms=2,
                      price_per_night=100.0, max_guests=4, amenity_ids=["1", "2"])
        self.data_manager.save(place)
        deleted = self.data_manager.delete(place.place_id)
        self.assertTrue(deleted)
        self.assertIsNone(self.repository.get(place.place_id))

    def test_get_all_places(self):
        place1 = Place(name="Place 1", description="Nice place 1", address="123 Street", city_id=1,
                       latitude=45.0, longitude=-75.0, host_id=1, number_of_rooms=3, number_of_bathrooms=2,
                       price_per_night=100.0, max_guests=4, amenity_ids=["1", "2"])
        place2 = Place(name="Place 2", description="Nice place 2", address="456 Avenue", city_id=2,
                       latitude=46.0, longitude=-76.0, host_id=2, number_of_rooms=4, number_of_bathrooms=3,
                       price_per_night=150.0, max_guests=6, amenity_ids=["3", "4"])
        self.data_manager.save(place1)
        self.data_manager.save(place2)
        all_places = self.data_manager.get_all_places()
        self.assertEqual(len(all_places), 2)
        self.assertIn(place1, all_places)
        self.assertIn(place2, all_places)

    def test_create_place(self):
        place_data = {
            "name": "New Place",
            "description": "A new place",
            "address": "789 Boulevard",
            "city_id": 3,
            "latitude": 47.0,
            "longitude": -77.0,
            "host_id": 3,
            "number_of_rooms": 5,
            "number_of_bathrooms": 4,
            "price_per_night": 200.0,
            "max_guests": 8,
            "amenity_ids": ["5", "6"]
        }
        place_id = self.data_manager.create_place(place_data)
        place = self.data_manager.get(place_id)
        self.assertEqual(place.name, "New Place")
        self.assertEqual(place.place_id, place_id)

    def test_update_nonexistent_place(self):
        result = self.data_manager.update(999, {"name": "Updated Place"})
        self.assertFalse(result)

    def test_delete_nonexistent_place(self):
        result = self.data_manager.delete(999)
        self.assertFalse(result)

    def test_get_nonexistent_place(self):
        place = self.data_manager.get(999)
        self.assertIsNone(place)

if __name__ == '__main__':
    unittest.main()
