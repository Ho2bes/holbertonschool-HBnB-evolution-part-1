# test2/test_amenity_api.py

import unittest
import sys
import os

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from flask_restx import Api
from api.amenity_api import api as amenity_api
from data_manager import DataManager

class TestAmenityAPI(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(amenity_api, path='/amenities')
        self.client = self.app.test_client()

    def test_get_all_amenities(self):
        response = self.client.get('/amenities/')
        self.assertEqual(response.status_code, 200)

    def test_create_amenity(self):
        new_amenity = {
            'name': 'Swimming Pool'
        }
        response = self.client.post('/amenities/', json=new_amenity)
        self.assertEqual(response.status_code, 201)

    # Ajoutez des tests pour d'autres méthodes de l'API Amenity

if __name__ == '__main__':
    unittest.main()
