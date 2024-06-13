#!/usr/bin/python3

import unittest
from place_7.model.review import Review  # Import correct depuis MY_Review.model

class TestReview(unittest.TestCase):
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
        # Vérification des attributs avant la suppression
        self.assertIsNotNone(self.review.review_id)
        self.assertIsNotNone(self.review.feedback)
        self.assertIsNotNone(self.review.rating)

        # Suppression de la revue
        self.review.delete_review()

        # Vérification des attributs après la suppression
        self.assertIsNone(self.review.review_id)
        self.assertIsNone(self.review.feedback)
        self.assertIsNone(self.review.rating)

if __name__ == '__main__':
    unittest.main()
