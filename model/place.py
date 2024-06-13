#!/usr/bin/python3
"""Model for representing places"""

from datetime import datetime
import uuid


class Place:
    """Class representing a place."""
    def __init__(self, name, description, address, city_id, latitude,
                 longitude, host_id, number_of_rooms, number_of_bathrooms,
                 price_per_night, max_guests, amenity_ids):
        self.place_id = str(uuid.uuid4())
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
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns the place data as a dictionary."""
        return {
            'place_id': self.place_id,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'city_id': self.city_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'host_id': self.host_id,
            'number_of_rooms': self.number_of_rooms,
            'number_of_bathrooms': self.number_of_bathrooms,
            'price_per_night': self.price_per_night,
            'max_guests': self.max_guests,
            'amenity_ids': self.amenity_ids,
            'reviews': self.reviews,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def update_place_data(self, new_data):
        """Updates place data with new values."""
        for key, value in new_data.items():
            setattr(self, key, value)
        self.updated_at = datetime.now()
