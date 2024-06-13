# test2/test_country_api.py

import unittest
import sys
import os

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from flask_restx import Api
from api.country_api import api as country_api
from data_manager import DataManager

class TestCountryAPI(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(country_api, path='/countries')
        self.client = self.app.test_client()

    def test_get_all_countries(self):
        response = self.client.get('/countries/')
        self.assertEqual(response.status_code, 200)

    def test_create_country(self):
        new_country = {
            'name': 'USA'
        }
        response = self.client.post('/countries/', json=new_country)
        self.assertEqual(response.status_code, 201)

    # Ajoutez des tests pour d'autres méthodes de l'API Country

if __name__ == '__main__':
    unittest.main()
