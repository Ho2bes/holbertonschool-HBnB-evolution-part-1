#!/usr/bin/python3


import unittest
import json
from flask import Flask
from place_route import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_get_places(self):
        response = self.client.get('/places')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_create_place(self):
        new_place_data = {
            'name': 'New Place',
            'location': 'New Location',
            'description': 'New Description'
        }
        response = self.client.post('/places', json=new_place_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Lieu créé avec succès')

    # Ajoutez d'autres méthodes de test pour les autres routes (GET /places/<place_id>, PUT /places/<place_id>, DELETE /places/<place_id>)

if __name__ == '__main__':
    unittest.main()
