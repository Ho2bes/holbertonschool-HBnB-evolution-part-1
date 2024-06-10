#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)
data_manager = DataManager()

class Review:
    def __init__(self, review_id, feedback, rating):
        self.review_id = review_id
        self.feedback = feedback
        self.rating = rating

    def edit_feedback(self, new_feedback):
        self.feedback = new_feedback

    def edit_rating(self, new_rating):
        self.rating = new_rating

@app.route('/api/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    review_id = len(data_manager.storage.get('Review', {})) + 1
    feedback = data.get('feedback')
    rating = data.get('rating')

    review = Review(review_id, feedback, rating)
    data_manager.save(review)

    return jsonify({'message': 'Review created successfully'}), 201

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    reviews = data_manager.storage.get('Review', {}).values()
    return jsonify({'reviews': [review.__dict__ for review in reviews]})

if __name__ == '__main__':
    app.run(debug=True)
