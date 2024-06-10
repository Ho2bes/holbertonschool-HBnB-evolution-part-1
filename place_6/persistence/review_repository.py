#!/usr/bin/python3


from persistence.ipersistence_manager import IPersistenceManager
from model.review import Review

class ReviewRepository(IPersistenceManager):
    """Classe pour gérer la persistance des avis."""
    def __init__(self):
        self.reviews = {}
        self.next_id = 1

    def save(self, review):
        """Sauvegarde un avis."""
        if not hasattr(review, 'review_id'):
            review.review_id = self.next_id
            self.next_id += 1
        self.reviews[review.review_id] = review

    def get(self, review_id):
        """Récupère un avis."""
        return self.reviews.get(review_id)

    def get_all(self):
        """Récupère tous les avis."""
        return list(self.reviews.values())

    def update(self, review_id, new_review_data):
        """Met à jour un avis existant."""
        if review_id in self.reviews:
            review = self.reviews[review_id]
            for key, value in new_review_data.items():
                setattr(review, key, value)
            self.save(review)
            return True
        return False

    def delete(self, review_id):
        """Supprime un avis existant."""
        if review_id in self.reviews:
            del self.reviews[review_id]
            return True
        return False
