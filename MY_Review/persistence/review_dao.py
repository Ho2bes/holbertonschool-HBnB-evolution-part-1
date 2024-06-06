#!/usr/bin/python3

class Review:
    def __init__(self, review_id, feedback, rating):
        self.review_id = review_id
        self.feedback = feedback
        self.rating = rating

    def edit_feedback(self, new_feedback):
        self.feedback = new_feedback

    def edit_rating(self, new_rating):
        self.rating = new_rating

    def delete_review(self):
        # Code pour supprimer la revue de la base de données ou du stockage
        pass # i
