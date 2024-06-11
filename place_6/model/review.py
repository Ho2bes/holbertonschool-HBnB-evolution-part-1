#!/usr/bin/python3
"""Modèle pour la représentation des avis."""

class Review:
    def __init__(self, user_id, place_id, rating, comment):
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment

    def update_review_data(self, new_data):
        for key, value in new_data.items():
            setattr(self, key, value)

