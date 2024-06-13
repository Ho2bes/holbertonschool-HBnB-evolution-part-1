#!/usr/bin/python3

import unittest
from User_review import Review

class test_user_review(unittest.TestCase):
    def setUp(self):
        # Initialisation pour chaque test avec des valeurs par défaut
        self.review = Review("Initial feedback", 3)

    def test_set_feedback(self):
        # Test de modification de l'avis
        self.review.set_feedback("Great product")
        self.assertEqual(self.review.get_feedback(), "Great product")

    def test_set_rating(self):
        # Test de modification de la note
        self.review.set_rating(5)
        self.assertEqual(self.review.get_rating(), 5)

    def test_edit_feedback(self):
        # Test de modification de l'avis avec méthode dédiée
        self.review.edit_feedback("Awesome product")
        self.assertEqual(self.review.get_feedback(), "Awesome product")

if __name__ == '__main__':
    unittest.main()
