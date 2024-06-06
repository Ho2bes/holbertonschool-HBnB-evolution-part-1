#!/usr/bin/python3
"""Modèle pour la représentation des lieux."""

class Place:
    """Classe représentant un lieu."""
    def __init__(self, location, number_guests, number_rooms):
        self.location = location
        self.number_guests = number_guests
        self.number_rooms = number_rooms
        self.reviews = []
        self.amenities = []
        self.description = ""
        self.availability = True
        self.host = None

    def add_review(self, review):
        """Ajoute un commentaire."""
        self.reviews.append(review)

    def calculate_total_price(self, nightly_rate):
        """Calcule le prix total."""
        return nightly_rate * self.number_guests

    def list_amenities(self):
        """Liste les équipements."""
        return self.amenities

    def check_availability(self):
        """Vérifie la disponibilité."""
        return self.availability

    def list_reviews(self):
        """Liste les commentaires."""
        return self.reviews

    def set_number_of_guests(self, number):
        """Définit le nombre d'invités."""
        self.number_guests = number

    def add_description(self, description):
        """Ajoute une description."""
        self.description = description

    def set_number_of_rooms(self, number):
        """Définit le nombre de chambres."""
        self.number_rooms = number

    def set_location(self, location):
        """Définit l'emplacement."""
        self.location = location

    def add_amenity(self, amenity):
        """Ajoute un équipement."""
        self.amenities.append(amenity)

    def toggle_availability(self):
        """Bascule la disponibilité."""
        self.availability = not self.availability

    def get_description(self):
        """Récupère la description."""
        return self.description

    def get_location(self):
        """Récupère l'emplacement."""
        return self.location

    def update_place_data(self, new_data):
        """Met à jour les données du lieu avec de nouvelles données."""
        for key, value in new_data.items():
            setattr(self, key, value)

    def delete_amenity(self, amenity_id):
        """Supprime un équipement du lieu par son ID."""
        for amenity in self.amenities:
            if amenity.id == amenity_id:
                self.amenities.remove(amenity)
                break
