import unittest
from flask import Flask, jsonify
from unittest.mock import MagicMock
from api.place_routes import app

class TestPlaceRoutes(unittest.TestCase):
    def setUp(self):
        # Création d'une application Flask test
        self.app = app.test_client()

        # Mock de PlaceRepository pour simuler la persistance des données
        self.mock_repo = MagicMock()
        app.place_repo = self.mock_repo

    def test_get_place_existing(self):
        # Test de la route pour récupérer un lieu existant
        self.mock_repo.get_place.return_value = {'location': 'Paris', 'number_guests': 4, 'number_rooms': 2}
        response = self.app.get('/places/123')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'location': 'Paris', 'number_guests': 4, 'number_rooms': 2})

    def test_get_place_nonexistent(self):
        # Test de la route pour récupérer un lieu inexistant
        self.mock_repo.get_place.return_value = None
        response = self.app.get('/places/456')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'error': 'Place not found'})

if __name__ == '__main__':
    unittest.main()
