#!/usr/bin/python3
"""Modèle pour la représentation des villes."""

class City:
    def __init__(self, name, country_id):
        self.name = name
        self.country_id = country_id

    def update_city_data(self, new_data):
        for key, value in new_data.items():
            setattr(self, key, value)

