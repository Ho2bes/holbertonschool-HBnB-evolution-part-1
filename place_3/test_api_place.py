#!/usr/bin/python3

import unittest
from flask import Flask, json
from api_place import app, PlaceRepository

class TestPlaceAPI(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        # Configuration initiale avant chaque test
        self.client = self.app.test_client()
        self.place_data = {
            'name': 'Place Test',
            'description': 'Description du lieu',
            'address': 'Adresse du lieu',
            'city_id': 1,
            'latitude': 10.0,
            'longitude': 20.0,
            'host_id': 1,
            'number_of_rooms': 2,
            'number_of_bathrooms': 1,
            'price_per_night': 100.0,
            'max_guests': 4,
            'amenity_ids': ['wifi', 'parking']
        }

    def test_get_all_places(self):
        response = self.client.get('/places')
        self.assertEqual(response.status_code, 200)

    def test_create_place(self):
        response = self.client.post('/places', data=json.dumps(self.place_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('place_id', response.json)

    def test_get_place(self):
        # Créez d'abord un lieu pour tester la récupération
        post_response = self.client.post('/places', data=json.dumps(self.place_data), content_type='application/json')
        place_id = post_response.json['place_id']

        response = self.client.get(f'/places/{place_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], self.place_data['name'])

    def test_delete_place(self):
        # Créez d'abord un lieu pour tester la suppression
        post_response = self.client.post('/places', data=json.dumps(self.place_data), content_type='application/json')
        place_id = post_response.json['place_id']

        response = self.client.delete(f'/places/{place_id}')
        self.assertEqual(response.status_code, 204)

        # Vérifiez que le lieu a été supprimé
        get_response = self.client.get(f'/places/{place_id}')
        self.assertEqual(get_response.status_code, 404)

    def test_update_place(self):
        # Créez d'abord un lieu pour tester la mise à jour
        post_response = self.client.post('/places', data=json.dumps(self.place_data), content_type='application/json')
        place_id = post_response.json['place_id']

        updated_data = self.place_data.copy()
        updated_data['name'] = 'Updated Place'

        response = self.client.put(f'/places/{place_id}', data=json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, 204)

        # Vérifiez que le lieu a été mis à jour
        get_response = self.client.get(f'/places/{place_id}')
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(get_response.json['name'], 'Updated Place')

if __name__ == '__main__':
    unittest.main()
