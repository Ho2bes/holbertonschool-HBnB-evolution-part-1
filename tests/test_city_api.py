import unittest
import sys
import os
from flask import Flask
from flask_restx import Api
from api.city_api import api as city_api

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestCityAPI(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(city_api, path='/cities')
        self.client = self.app.test_client()

    def test_get_all_cities(self):
        response = self.client.get('/cities/')
        self.assertEqual(response.status_code, 200)

    def test_create_city(self):
        new_city = {
            'name': 'New York',
            'country_id': '1'
        }
        response = self.client.post('/cities/', json=new_city)
        self.assertEqual(response.status_code, 201)

    # Ajoutez des tests pour d'autres méthodes de l'API City


if __name__ == '__main__':
    unittest.main()
