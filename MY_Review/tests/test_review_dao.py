#!/usr/bin/python3

import unittest
from unittest.mock import patch
from MY_Review.persistence.review_dao import Review

class TestReviewDAO(unittest.TestCase):
    def setUp(self):
        # Initialisation pour chaque test
        self.review = Review(1, "Great product", 5)

    def test_edit_feedback(self):
        # Test de modification du feedback
        self.review.edit_feedback("Amazing product")
        self.assertEqual(self.review.feedback, "Amazing product")

    def test_edit_rating(self):
        # Test de modification de la note
        self.review.edit_rating(4)
        self.assertEqual(self.review.rating, 4)

    def test_delete_review(self):
        # Implémenter la logique de suppression de la revue ici
        self.review_id = None
        self.feedback = None
        self.rating = None

if __name__ == '__main__':
    unittest.main()
