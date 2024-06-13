# test2/test_user_api.py

import unittest
import sys
import os

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from flask_restx import Api
from api.user_api import api as user_api
from data_manager import DataManager

class TestUserAPI(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(user_api, path='/users')
        self.client = self.app.test_client()

    def test_get_all_users(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        new_user = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password'
        }
        response = self.client.post('/users/', json=new_user)
        self.assertEqual(response.status_code, 201)

    # Ajoutez des tests pour d'autres méthodes de l'API User

if __name__ == '__main__':
    unittest.main()
