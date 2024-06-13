# test2/test_review_api.py

import unittest
import sys
import os

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from flask_restx import Api
from api.review_api import api as review_api
from data_manager import DataManager

class TestReviewAPI(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_namespace(review_api, path='/reviews')
        self.client = self.app.test_client()

    def test_get_all_reviews(self):
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, 200)

    def test_create_review(self):
        new_review = {
            'user_id': '1',
            'place_id': '1',
            'rating': 5,
            'comment': 'Great place!'
        }
        response = self.client.post('/reviews/', json=new_review)
        self.assertEqual(response.status_code, 201)

    # Ajoutez des tests pour d'autres méthodes de l'API Review

if __name__ == '__main__':
    unittest.main()
