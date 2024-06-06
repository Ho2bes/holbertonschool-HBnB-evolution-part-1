#!/usr/bin/python3

import unittest
from MY_Review.persistence.review_persistence_manager import ReviewPersistenceManager
from MY_Review.model.review import Review

class TestReviewPersistenceManager(unittest.TestCase):
    def setUp(self):
        self.manager = ReviewPersistenceManager()
        self.review = Review(1, "Great product", 5)
        self.manager.save(self.review)

    def test_save_review(self):
        review = self.manager.retrieve(1)
        self.assertIsNotNone(review)
        self.assertEqual(review.feedback, "Great product")

    def test_update_review(self):
        self.review.edit_feedback("Amazing product")
        self.manager.update(self.review)
        review = self.manager.retrieve(1)
        self.assertEqual(review.feedback, "Amazing product")

    def test_delete_review(self):
        self.manager.delete(1)
        review = self.manager.retrieve(1)
        self.assertIsNone(review)

if __name__ == '__main__':
    unittest.main()
