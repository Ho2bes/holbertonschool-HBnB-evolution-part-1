#!/usr/bin/python3

from IPersistence_Manager import IPersistenceManager

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

# Classe Review pour tester
class Review:
    def __init__(self, review_id, feedback, rating):
        self.review_id = review_id
        self.feedback = feedback
        self.rating = rating

    def edit_feedback(self, new_feedback):
        self.feedback = new_feedback

    def edit_rating(self, new_rating):
        self.rating = new_rating

# Exemple d'utilisation
if __name__ == "__main__":
    manager = ReviewPersistenceManager()
    review = Review(1, "Great product!", 5)
    manager.save(review)
    retrieved_review = manager.retrieve(1)
    print(retrieved_review.feedback)  # Output: Great product!
    review.edit_feedback("Updated feedback")
    manager.update(review)
    updated_review = manager.retrieve(1)
    print(updated_review.feedback)  # Output: Updated feedback
    manager.delete(1)
    print(manager.retrieve(1))  # Output: None
