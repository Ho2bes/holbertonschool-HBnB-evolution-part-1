#!/usr/bin/python3
"class and methods of place for HBnB"


class Place:
    """class place with his methods"""
    def __init__(self, location, number_guests, number_rooms):
        self._location = location
        self._number_guests = number_guests
        self._number_rooms = number_rooms
        self._reviews = []
        self._amenities = []
        self._description = ""
        self._availability = True

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def number_guests(self):
        return self._number_guests

    @number_guests.setter
    def number_guests(self, value):
        self._number_guests = value

    @property
    def number_rooms(self):
        return self._number_rooms

    @number_rooms.setter
    def number_rooms(self, value):
        self._number_rooms = value

    @property
    def reviews(self):
        return self._reviews

    @property
    def amenities(self):
        return self._amenities

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def availability(self):
        return self._availability

    @availability.setter
    def availability(self, value):
        self._availability = value

    def add_review(self, review):
        self._reviews.append(review)

    def add_amenity(self, amenity):
        self._amenities.append(amenity)

    def toggle_availability(self):
        self._availability = not self._availability

    def calculate_total_price(self, nightly_rate):
        return nightly_rate * self._number_guests  # Supposons que le prix soit calculé par nuit

    def list_reviews(self):
        return self._reviews
