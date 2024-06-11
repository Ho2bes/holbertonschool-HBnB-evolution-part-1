#!/usr/bin/python3
"""Modèle pour la représentation des équipements."""

class Amenity:
    def __init__(self, name):
        self.name = name

    def update_amenity_data(self, new_data):
        for key, value in new_data.items():
            setattr(self, key, value)

