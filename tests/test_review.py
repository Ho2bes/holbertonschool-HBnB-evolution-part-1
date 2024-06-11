import unittest
from model.review import Review
from persistence.data_manager import ReviewRepository

class TestReviewModel(unittest.TestCase):

    def setUp(self):
        self.review_repo = ReviewRepository()
        self.review_data = {
            'user_id': 'user1',
            'place_id': 'place1',
            'rating': 5,
            'comment': 'Excellent place!'
        }

    def test_create_review(self):
        review = Review(self.review_data['user_id'], self.review_data['place_id'], self.review_data['rating'], self.review_data['comment'])
        self.review_repo.save(review)
        saved_review = self.review_repo.get(review.review_id)
        self.assertEqual(saved_review.comment, self.review_data['comment'])

    def test_update_review(self):
        review = Review(self.review_data['user_id'], self.review_data['place_id'], self.review_data['rating'], self.review_data['comment'])
        self.review_repo.save(review)
        new_data = {'comment': 'Updated comment'}
        self.review_repo.update(review.review_id, new_data)
        updated_review = self.review_repo.get(review.review_id)
        self.assertEqual(updated_review.comment, 'Updated comment')

    def test_delete_review(self):
        review = Review(self.review_data['user_id'], self.review_data['place_id'], self.review_data['rating'], self.review_data['comment'])
        self.review_repo.save(review)
        self.review_repo.delete(review.review_id)
        deleted_review = self.review_repo.get(review.review_id)
        self.assertIsNone(deleted_review)

if __name__ == '__main__':
    unittest.main()
