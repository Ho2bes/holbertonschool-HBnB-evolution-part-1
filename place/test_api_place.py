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
        self.assertEqual(response.status_code, 200)
        # Ajoutez des assertions supplémentaires pour vérifier les données du lieu récupéré

    def test_get_place_nonexistent(self):
        response = self.app.get('/places/999')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'Lieu non trouvé')

    # Ajoutez d'autres méthodes de test pour les autres routes

if __name__ == '__main__':
    unittest.main()
