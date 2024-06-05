#!/usr/bin/python3
"class and methods of place for HBnB"


class Place:
    """class place with his methods"""
    def __init__(self, location, number_guests, number_rooms):
        self.location = location
        self.number_guests = number_guests
        self.number_rooms = number_rooms
        self.reviews = []
        self.amenities = []
        self.description = ""
        self.availability = True

    def add_review(self, review):
        self.reviews.append(review)

    def calculate_total_price(self, nightly_rate):
        return nightly_rate * self.number_guests  # Supposons que le prix soit calculé par nuit

    def list_amenities(self):
        return self.amenities

    def check_availability(self):
        return self.availability

    def list_reviews(self):
        return self.reviews

    def set_number_guests(self, number):
        self.number_guests = number

    def add_description(self, description):
        self.description = description

    def set_number_rooms(self, number):
        self.number_rooms = number

    def set_location(self, location):
        self.location = location

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

    def toggle_availability(self):
        self.availability = not self.availability

    def get_description(self):
        return self.description

    def get_location(self):
        return self.location
