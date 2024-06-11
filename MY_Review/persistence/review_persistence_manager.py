#!/usr/bin/python3

from persistence_manager import IPersistenceManager

class ReviewPersistenceManager(IPersistenceManager):
    def __init__(self):
        self.reviews = {}

    def save(self, review):
        self.reviews[review.review_id] = review

    def retrieve(self, review_id):
        return self.reviews.get(review_id, None)

    def update(self, review):
        if review.review_id in self.reviews:
            self.reviews[review.review_id] = review

    def delete(self, review_id):
        if review_id in self.reviews:
            del self.reviews[review_id]
