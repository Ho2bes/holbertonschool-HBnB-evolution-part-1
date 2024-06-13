import unittest
import os
import sys
import json
from unittest.mock import patch

# Ajouter le répertoire parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from flask import Flask
from flask_restx import Api
from api.amenity_api import amenity_blueprint
from model.amenity import Amenity
from persistence.amenity_repository import AmenityRepository

class TestAmenityAPI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['DEBUG'] = False
        self.api = Api(self.app)
        self.api.init_app(self.app)
        self.app.register_blueprint(amenity_blueprint, url_prefix='/')
        self.client = self.app.test_client()
        self.amenity_data = {
            'name': 'WiFi'
        }
        self.updated_amenity_data = {
            'name': 'Updated WiFi'
        }

    @patch.object(AmenityRepository, 'get_all')
    def test_get_all_amenities(self, mock_get_all):
        mock_get_all.return_value = [Amenity(name='WiFi')]
        response = self.client.get('/amenities')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0]['name'], 'WiFi')

    @patch.object(AmenityRepository, 'save')
    def test_create_amenity(self, mock_save):
        mock_save.return_value = '12345'
        response = self.client.post('/amenities', data=json.dumps(self.amenity_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('12345', response.json['amenity_id'])

    @patch.object(AmenityRepository, 'get')
    def test_get_amenity(self, mock_get):
        amenity = Amenity(name='WiFi')
        amenity.amenity_id = '12345'
        mock_get.return_value = amenity
        response = self.client.get('/amenities/12345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['amenity_id'], '12345')
        self.assertEqual(response.json['name'], 'WiFi')

    @patch.object(AmenityRepository, 'update')
    def test_update_amenity(self, mock_update):
        mock_update.return_value = True
        response = self.client.put('/amenities/12345', data=json.dumps(self.updated_amenity_data), content_type='application/json')
        self.assertEqual(response.status_code, 204)

    @patch.object(AmenityRepository, 'delete')
    def test_delete_amenity(self, mock_delete):
        mock_delete.return_value = True
        response = self.client.delete('/amenities/12345')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
