#!/usr/bin/python3

import unittest

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        self.review = Review(1, "Great product!", 5)

    def test_save(self):
        self.data_manager.save(self.review)
        self.assertIn(1, self.data_manager.storage['Review'])

    def test_get(self):
        self.data_manager.save(self.review)
        fetched_review = self.data_manager.get(1, 'Review')
        self.assertEqual(fetched_review.feedback, "Great product!")

    def test_update(self):
        self.data_manager.save(self.review)
        self.review.edit_feedback("Updated feedback")
        self.data_manager.update(self.review)
        updated_review = self.data_manager.get(1, 'Review')
        self.assertEqual(updated_review.feedback, "Updated feedback")

    def test_delete(self):
        self.data_manager.save(self.review)
        self.data_manager.delete(1, 'Review')
        deleted_review = self.data_manager.get(1, 'Review')
        self.assertIsNone(deleted_review)

if __name__ == '__main__':
    unittest.main()
