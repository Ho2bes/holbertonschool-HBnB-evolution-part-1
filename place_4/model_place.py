#!/usr/bin/python3
"""Modèle pour la représentation des lieux."""

class Place:
    """Classe représentant un lieu."""
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
        """Ajoute un commentaire."""
        self.reviews.append(review)

    def calculate_total_price(self):
        """Calcule le prix total."""
        return self.price_per_night * self.max_guests

    def list_amenities(self):
        """Liste les équipements."""
        return self.amenity_ids

    def check_availability(self):
        """Vérifie la disponibilité."""
        # Logique pour vérifier la disponibilité
        pass

    def list_reviews(self):
        """Liste les commentaires."""
        return self.reviews

    def set_number_of_guests(self, number):
        """Définit le nombre d'invités."""
        self.max_guests = number

    def add_description(self, description):
        """Ajoute une description."""
        self.description = description

    def set_number_of_rooms(self, number):
        """Définit le nombre de chambres."""
        self.number_of_rooms = number

    def set_location(self, latitude, longitude):
        """Définit l'emplacement."""
        self.latitude = latitude
        self.longitude = longitude

    def add_amenity(self, amenity_id):
        """Ajoute un équipement."""
        self.amenity_ids.append(amenity_id)

    def toggle_availability(self):
        """Bascule la disponibilité."""
        # Logique pour basculer la disponibilité
        pass

    def get_description(self):
        """Récupère la description."""
        return self.description

    def get_location(self):
        """Récupère l'emplacement."""
        return self.latitude, self.longitude

    def update_place_data(self, new_data):
        """Met à jour les données du lieu avec de nouvelles données."""
        for key, value in new_data.items():
            setattr(self, key, value)

    def delete_amenity(self, amenity_id):
        """Supprime un équipement du lieu par son ID."""
        if amenity_id in self.amenity_ids:
            self.amenity_ids.remove(amenity_id)

