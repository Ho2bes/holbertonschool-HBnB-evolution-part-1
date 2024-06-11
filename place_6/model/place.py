#!/usr/bin/python3
"""Modèle pour la représentation des lieux."""

class Place:
    def __init__(self, name, description, address, city_id, latitude, longitude, host_id, number_of_rooms, number_of_bathrooms, price_per_night, max_guests, amenity_ids):
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenity_ids = amenity_ids
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def calculate_total_price(self):
        return self.price_per_night * self.max_guests

    def list_amenities(self):
        return self.amenity_ids

    def check_availability(self):
        pass

    def list_reviews(self):
        return self.re
