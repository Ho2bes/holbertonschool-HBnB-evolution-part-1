#!/usr/bin/python3
"""unnistest"""


import unittest
from flask import Flask, jsonify
from unittest.mock import patch
from place_route import app

class TestPlaceRoutes(unittest.TestCase):
    def setUp(self):
        # Création d'une application Flask test
        self.app = app.test_client()

    @patch('api.place_routes.place_repo')  # Mock de PlaceRepository
    def test_get_place_existing(self, mock_repo):
        # Données de test
        place_data = {'location': 'Paris', 'number_guests': 4, 'number_rooms': 2}
        mock_repo.get_place.return_value = place_data

        # Test de la route pour récupérer un lieu existant
        response = self.app.get('/places/123')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, place_data)

    @patch('api.place_routes.place_repo')  # Mock de PlaceRepository
    def test_get_place_nonexistent(self, mock_repo):
        # Mock de la méthode get_place pour retourner None (lieu inexistant)
        mock_repo.get_place.return_value = None

        # Test de la route pour récupérer un lieu inexistant
        response = self.app.get('/places/456')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'error': 'Place not found'})

if __name__ == '__main__':
    unittest.main()
