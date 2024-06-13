#!/usr/bin/python3
# API for managing countries

from flask_restx import Namespace, Resource, fields
from data_manager import DataManager

api = Namespace('countries', description='Country related operations')

data_manager = DataManager()

# Data model for displaying a country
country_model = api.model('Country', {
    'country_id': fields.String(description='Country ID'),
    'name': fields.String(required=True, description='Country name'),
    'created_at': fields.DateTime(description='Creation date'),
    'updated_at': fields.DateTime(description='Last update date')
})

@api.route('/')
class Countries(Resource):
    @api.marshal_list_with(country_model)
    def get(self):
        """Retrieve all countries."""
        all_countries = data_manager.get_all_countries()
        return all_countries
