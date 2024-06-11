#!/usr/bin/python3


from flask import Blueprint
from flask_restx import Api

# Créer un blueprint pour l'API
api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp, doc='/docs')

# Importer les modules pour enregistrer les routes
from .api_amenity import api as amenity_api
from .api_city import api as city_api
from .api_country import api as country_api
from .api_place import api as place_api
from .api_review import api as review_api
from .api_user import api as user_api

# Ajouter les namespaces au Blueprint
api.add_namespace(amenity_api, path='/amenities')
api.add_namespace(city_api, path='/cities')
api.add_namespace(country_api, path='/countries')
api.add_namespace(place_api, path='/places')
api.add_namespace(review_api, path='/reviews')
api.add_namespace(user_api, path='/users')
