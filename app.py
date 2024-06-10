#!/usr/bin/python3

from flask import Flask, jsonify, request
from MY_Review.model.review import Review
from MY_Review.persistence.review_persistence_manager import ReviewPersistenceManager

app = Flask(__name__)

# Exemple de données factices pour simuler une base de données de revues
reviews_db = ReviewPersistenceManager()

# Route pour créer une nouvelle revue
@app.route('/api/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    review_id = len(reviews_db.reviews) + 1  # Simuler l'auto-incrément de l'ID
    feedback = data.get('feedback')
    rating = data.get('rating')

    review = Review(review_id, feedback, rating)
    reviews_db.save(review)

    return jsonify({'message': 'Review created successfully'}), 201

# Route pour récupérer toutes les revues
@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    return jsonify({'reviews': [review.__dict__ for review in reviews_db.reviews.values()]})

if __name__ == '__main__':
    app.run(debug=True)
