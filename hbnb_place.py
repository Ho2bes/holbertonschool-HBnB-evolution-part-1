#!/usr/bin/python3
"class and methods of place for HBnB"


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
        self.host = None  # Nouvel attribut pour stocker l'hôte du lieu

    def add_review(self, review):
        """Ajoute un commentaire."""
        self.reviews.append(review)

    def calculate_total_price(self, nightly_rate):
        """Calcule le prix total."""
        return nightly_rate * self.number_guests  # Supposons que le prix soit calculé par nuit

    def list_amenities(self):
        """Liste les équipements."""
        return self.amenities

    def check_availability(self):
        """Vérifie la disponibilité."""
        return self.availability

    def list_reviews(self):
        """Liste les commentaires."""
        return self.reviews

    def set_number_guests(self, number):
        """Définit le nombre d'invités."""
        self.number_guests = number

    def add_description(self, description):
        """Ajoute une description."""
        self.description = description

    def set_number_rooms(self, number):
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

