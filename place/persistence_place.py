
#!/usr/bin/python3
"""Code de persistance pour la classe Place."""

class PlaceRepository:
    """Classe pour gérer la persistance des lieux."""
    def __init__(self):
        self.places = {}

    def save_place(self, place_id, place_data):
        """Sauvegarde un lieu."""
        self.places[place_id] = place_data

    def get_place(self, place_id):
        """Récupère un lieu."""
        return self.places.get(place_id)

    def get_all_places(self):
        """Récupère tous les lieux."""
        return list(self.places.values())

    def create_place(self, place_data):
        """Crée un nouveau lieu."""
        place_id = len(self.places) + 1
        self.places[place_id] = place_data
        return place_id

    def update_place(self, place_id, new_place_data):
        """Met à jour un lieu existant."""
        if place_id in self.places:
            self.places[place_id] = new_place_data
            return True
        else:
            return False

    def delete_place(self, place_id):
        """Supprime un lieu existant."""
        if place_id in self.places:
            del self.places[place_id]
            return True
        else:
            return False

    # D'autres méthodes CRUD peuvent être ajoutées ici
