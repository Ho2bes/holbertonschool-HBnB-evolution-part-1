import unittest
import sys
import os
from flask import Flask
from flask_restx import Api
from api.place_api import api as place_api

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestPlaceAPI(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(place_api, path='/places')
        self.client = self.app.test_client()

    def test_get_all_places(self):
        response = self.client.get('/places/')
        self.assertEqual(response.status_code, 200)

    def test_create_place(self):
        new_place = {
            'name': 'Test Place',
            'description': 'A place for testing',
            'address': '123 Test St',
            'city_id': '1',
            'latitude': 40.7128,
            'longitude': -74.0060,
            'host_id': '1',
            'number_of_rooms': 3,
            'number_of_bathrooms': 2,
            'price_per_night': 100.0,
            'max_guests': 4,
            'amenity_ids': ['1', '2']
        }
        response = self.client.post('/places/', json=new_place)
        self.assertEqual(response.status_code, 201)

    # Ajoutez des tests pour d'autres méthodes de l'API Place


if __name__ == '__main__':
    unittest.main()
