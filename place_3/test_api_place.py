#!/usr/bin/python3

import unittest
from unittest.mock import patch
from api_place import app

class TestAPIPlace(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('api_place.place_data_manager.get_all_places')
    def test_get_all_places(self, mock_get_all_places):
        mock_get_all_places.return_value = []
        response = self.app.get('/places')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    @patch('api_place.place_data_manager.create_place')
    def test_create_place(self, mock_create_place):
        mock_create_place.return_value = 1
        place_data = {
            "name": "Place 1",
            "description": "A nice place",
            "address": "123 Street",
            "city_id": 1,
            "latitude": 45.0,
            "longitude": -75.0,
            "host_id": 1,
            "number_of_rooms": 3,
            "number_of_bathrooms": 2,
            "price_per_night": 100.0,
            "max_guests": 4,
            "amenity_ids": ["1", "2"]
        }
        response = self.app.post('/places', json=place_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'message': 'Lieu créé avec succès', 'place_id': 1})

    @patch('api_place.place_data_manager.get_place')
    def test_get_place(self, mock_get_place):
        mock_get_place.return_value = {
            "name": "Place 1",
            "description": "A nice place",
            "address": "123 Street",
            "city_id": 1,
            "latitude": 45.0,
            "longitude": -75.0,
            "host_id": 1,
            "number_of_rooms": 3,
            "number_of_bathrooms": 2,
            "price_per_night": 100.0,
            "max_guests": 4,
            "amenity_ids": ["1", "2"]
        }
        response = self.app.get('/places/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], "Place 1")

    @patch('api_place.place_data_manager.delete_place')
    def test_delete_place(self, mock_delete_place):
        mock_delete_place.return_value = True
        response = self.app.delete('/places/1')
        self.assertEqual(response.status_code, 204)

    @patch('api_place.place_data_manager.update_place')
    def test_update_place(self, mock_update_place):
        mock_update_place.return_value = True
        place_data = {
            "name": "Updated Place",
            "description": "Updated description",
            "address": "123 New Street",
            "city_id": 1,
            "latitude": 46.0,
            "longitude": -75.5,
            "host_id": 2,
            "number_of_rooms": 4,
            "number_of_bathrooms": 3,
            "price_per_night": 120.0,
            "max_guests": 5,
            "amenity_ids": ["1", "3"]
        }
        response = self.app.put('/places/1', json=place_data)
        self.assertEqual(response.status_code, 204)

    @patch('api_place.place_data_manager.get_place')
    def test_get_nonexistent_place(self, mock_get_place):
        mock_get_place.return_value = None
        response = self.app.get('/places/999')
        self.assertEqual(response.status_code, 404)

    @patch('api_place.place_data_manager.delete_place')
    def test_delete_nonexistent_place(self, mock_delete_place):
        mock_delete_place.return_value = False
        response = self.app.delete('/places/999')
        self.assertEqual(response.status_code, 404)

    @patch('api_place.place_data_manager.update_place')
    def test_update_nonexistent_place(self, mock_update_place):
        mock_update_place.return_value = False
        place_data = {
            "name": "Updated Place",
            "description": "Updated description",
            "address": "123 New Street",
            "city_id": 1,
            "latitude": 46.0,
            "longitude": -75.5,
            "host_id": 2,
            "number_of_rooms": 4,
            "number_of_bathrooms": 3,
            "price_per_night": 120.0,
            "max_guests": 5,
            "amenity_ids": ["1", "3"]
        }
        response = self.app.put('/places/999', json=place_data)
        self.assertEqual(response.status_code, 404)

    @patch('api_place.place_data_manager.create_place')
    def test_create_place_invalid_data(self, mock_create_place):
        place_data = {
            "description": "A nice place",
            "address": "123 Street",
            "city_id": 1
        }
        response = self.app.post('/places', json=place_data)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
