#!/usr/bin/python3


from .ipersistence_manager import IPersistenceManager
from model.review import Review

class ReviewRepository(IPersistenceManager):
    def __init__(self):
        self.reviews = {}
        self.next_id = 1

    def save(self, review):
        if not hasattr(review, 'review_id'):
            review.review_id = self.next_id
            self.next_id += 1
        self.reviews[review.review_id] = review

    def get(self, review_id):
        return self.reviews.get(review_id)

    def get_all(self):
        return list(self.reviews.values())

    def update(self, review_id, new_data):
        if review_id in self.reviews:
            review = self.reviews[review_id]
            review.update_review_data(new_data)
            self.save(review)
            return True
        return False

    def delete(self, review_id):
        if review_id in self.reviews:
            del self.reviews[review_id]
            return True
        return False
