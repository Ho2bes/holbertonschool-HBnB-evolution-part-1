#!/usr/bin/python3

import unittest
import json
import sys
import os
from unittest.mock import patch
from place_7.model.review import Review  # Import correct depuis MY_Review.api

# Ajouter le chemin du répertoire racine pour importer 'app'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

class TestReviewAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_create_review(self):
        with patch('app.reviews_db', []):
            # Envoi d'une requête POST pour créer une nouvelle revue
            data = {'feedback': 'Great product', 'rating': 5}
            response = self.app.post('/api/reviews', json=data)

            # Vérification du code de statut de la réponse
            self.assertEqual(response.status_code, 201)

            # Vérification du message de réussite dans la réponse JSON
            data = json.loads(response.data)
            self.assertEqual(data['message'], 'Review created successfully')

    def test_get_reviews(self):
        with patch('app.reviews_db', []):
            # Envoi d'une requête GET pour récupérer toutes les revues
            response = self.app.get('/api/reviews')

            # Vérification du code de statut de la réponse
            self.assertEqual(response.status_code, 200)

            # Vérification du format de la réponse JSON
            data = json.loads(response.data)
            self.assertIsInstance(data, dict)
            self.assertIn('reviews', data)
            self.assertIsInstance(data['reviews'], list)

if __name__ == '__main__':
    unittest.main()
