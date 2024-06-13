# test2/test_review_repository.py

import unittest
import sys
import os

# Ajoutez le répertoire parent au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.review import Review
from persistence.review_repository import ReviewRepository

class TestReviewRepository(unittest.TestCase):

    def setUp(self):
        self.repo = ReviewRepository()

    def test_save_review(self):
        review = Review(user_id='1', place_id='1', rating=5, comment='Great place!')
        self.repo.save(review)
        self.assertIn(review.review_id, self.repo.reviews)

    def test_get_review(self):
        review = Review(user_id='1', place_id='1', rating=5, comment='Great place!')
        self.repo.save(review)
        fetched = self.repo.get(review.review_id)
        self.assertEqual(fetched.comment, 'Great place!')

    def test_update_review(self):
        review = Review(user_id='1', place_id='1', rating=5, comment='Great place!')
        self.repo.save(review)
        update_data = {'comment': 'Updated comment'}
        self.repo.update(review.review_id, update_data)
        updated = self.repo.get(review.review_id)
        self.assertEqual(updated.comment, 'Updated comment')

    def test_delete_review(self):
        review = Review(user_id='1', place_id='1', rating=5, comment='Great place!')
        self.repo.save(review)
        self.repo.delete(review.review_id)
        self.assertIsNone(self.repo.get(review.review_id))

if __name__ == '__main__':
    unittest.main()
