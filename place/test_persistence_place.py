#!/usr/bin/python3


import unittest
from persistence.place_repository import PlaceRepository

class TestPlaceRepository(unittest.TestCase):
    def setUp(self):
        # Initialisation des données de test
        self.repository = PlaceRepository()
        self.place_id = '123'
        self.place_data = {'location': 'Paris', 'number_guests': 4, 'number_rooms': 2}

    def test_save_place(self):
        # Test de la méthode save_place
        self.repository.save_place(self.place_id, self.place_data)
        self.assertIn(self.place_id, self.repository.places)
        self.assertEqual(self.repository.places[self.place_id], self.place_data)

    def test_get_place(self):
        # Test de la méthode get_place
        self.repository.save_place(self.place_id, self.place_data)
        retrieved_place = self.repository.get_place(self.place_id)
        self.assertEqual(retrieved_place, self.place_data)

    def test_get_nonexistent_place(self):
        # Test de la méthode get_place avec un lieu inexistant
        retrieved_place = self.repository.get_place('456')
        self.assertIsNone(retrieved_place)

if __name__ == '__main__':
    unittest.main()
