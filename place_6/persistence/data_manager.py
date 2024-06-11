#!/usr/bin/python3


from .place_repository import PlaceRepository
from .user_repository import UserRepository
from .review_repository import ReviewRepository
from .amenity_repository import AmenityRepository
from .country_repository import CountryRepository
from .city_repository import CityRepository
from model.place import Place
from model.user import User
from model.review import Review
from model.amenity import Amenity
from model.country import Country
from model.city import City

class DataManager:
    def __init__(self):
        self.place_repository = PlaceRepository()
        self.user_repository = UserRepository()
        self.review_repository = ReviewRepository()
        self.amenity_repository = AmenityRepository()
        self.country_repository = CountryRepository()
        self.city_repository = CityRepository()

    # Methods for Place
    def save_place(self, place_data):
        place = Place(**place_data)
        self.place_repository.save(place)
        return place.place_id

    def get_all_places(self):
        return self.place_repository.get_all()

    def get_place(self, place_id):
        return self.place_repository.get(place_id)

    def update_place(self, place_id, new_data):
        return self.place_repository.update(place_id, new_data)

    def delete_place(self, place_id):
        return self.place_repository.delete(place_id)

    # Methods for User
    def save_user(self, user_data):
        user = User(**user_data)
        self.user_repository.save(user)
        return user.user_id

    def get_all_users(self):
        return self.user_repository.get_all()

    def get_user(self, user_id):
        return self.user_repository.get(user_id)

    def update_user(self, user_id, new_data):
        return self.user_repository.update(user_id, new_data)

    def delete_user(self, user_id):
        return self.user_repository.delete(user_id)

    # Methods for Review
    def save_review(self, review_data):
        review = Review(**review_data)
        self.review_repository.save(review)
        return review.review_id

    def get_all_reviews(self):
        return self.review_repository.get_all()

    def get_review(self, review_id):
        return self.review_repository.get(review_id)

    def update_review(self, review_id, new_data):
        return self.review_repository.update(review_id, new_data)

    def delete_review(self, review_id):
        return self.review_repository.delete(review_id)

    # Methods for Amenity
    def save_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repository.save(amenity)
        return amenity.amenity_id

    def get_all_amenities(self):
        return
