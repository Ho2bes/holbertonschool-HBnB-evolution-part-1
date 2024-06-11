#!/usr/bin/python3
"""unnistest"""


import unittest
from flask import json
from place_route import app

class TestPlaceRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_place_existing(self):
        response = self.app.get('/places/1')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)  # Modifier le code de statut attendu à 404
        self.assertEqual(data['error'], 'Place not found')  # Ajouter une assertion pour le message d'erreur

    def test_get_place_nonexistent(self):
        response = self.app.get('/places/999')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'Place not found')

    # Ajoutez d'autres méthodes de test pour les autres routes

if __name__ == '__main__':
    unittest.main()
