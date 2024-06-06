#!/usr/bin/python3

from flask import Flask, jsonify, request
from model.review import Review

app = Flask(__name__)

# Exemple de données factices pour simuler une base de données de revues
reviews_db = []

# Route pour créer une nouvelle revue
@app.route('/api/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    review_id = len(reviews_db) + 1  # Simuler l'auto-incrément de l'ID
    feedback = data.get('feedback')
    rating = data.get('rating')

    review = Review(review_id, feedback, rating)
    reviews_db.append(review)

    return jsonify({'message': 'Review created successfully'}), 201

# Route pour récupérer toutes les revues
@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    return jsonify({'reviews': [review.__dict__ for review in reviews_db]})

if __name__ == '__main__':
    app.run(debug=True)
