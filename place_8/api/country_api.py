#!/usr/bin/python3


# API for managing countries
from flask_restx import Namespace, Resource
from data_manager import DataManager

api = Namespace('countries', description='Countries related operations')
data_manager = DataManager()

# Route for managing countries
@api.route('/')
class Countries(Resource):
    def get(self):
        """Fetches all countries."""
        return data_manager.get_all_countries()

@api.route('/<string:country_code>')
class CountryResource(Resource):
    def get(self, country_code):
        """Fetches a country by its code."""
        country = data_manager.get_country(country_code)
        if country:
            return country
        else:
            api.abort(404, "Country not found")

@api.route('/<string:country_code>/cities')
class CountryCities(Resource):
    def get(self, country_code):
        """Fetches all cities belonging to a specific country."""
        return data_manager.get_cities_by_country(country_code)
