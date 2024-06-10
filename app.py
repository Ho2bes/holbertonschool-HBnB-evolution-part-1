#!/usr/bin/python3
"""Point d'entrée principal pour l'application Flask."""

from flask import Flask
from flask_restx import Api
from api.user import api as user_api
from api.place import api as place_api
from api.amenity import api as amenity_api
from api.review import api as review_api
from api.country_city import api as country_city_api

app = Flask(__name__)
app.config['RESTX_MASK_SWAGGER'] = False

# Initialisation de l'API Flask-RESTx
api = Api(app, version='1.0', title='HBnB Evolution API', description='API pour HBnB Evolution')

# Ajout des namespaces pour les utilisateurs, les lieux, les équipements, les avis et les villes/pays
api.add_namespace(user_api, path='/api/v1/users')
api.add_namespace(place_api, path='/api/v1/places')
api.add_namespace(amenity_api, path='/api/v1/amenities')
api.add_namespace(review_api, path='/api/v1/reviews')
api.add_namespace(country_city_api, path='/api/v1')

@app.route('/')
def index():
    return 'Bienvenue sur l\'API HBnB Evolution!'

if __name__ == "__main__":
    app.run(debug=True)
