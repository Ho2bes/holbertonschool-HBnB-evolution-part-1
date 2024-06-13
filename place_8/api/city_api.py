#!/usr/bin/python3
# API for managing cities

from flask import request
from flask_restx import Namespace, Resource, fields
from data_manager import DataManager

api = Namespace('cities', description='City related operations')

data_manager = DataManager()

# Data model for creating a city
city_model = api.model('City', {
    'name': fields.String(required=True, description='City name'),
    'country_id': fields.String(required=True, description='Country ID')
})

# Extended model to include created_at and updated_at
city_model_extended = api.inherit('CityExtended', city_model, {
    'city_id': fields.String(description='City ID'),
    'created_at': fields.DateTime(description='Creation date'),
    'updated_at': fields.DateTime(description='Last update date')
})

@api.route('/')
class Cities(Resource):
    @api.marshal_list_with(city_model_extended)
    def get(self):
        """Retrieve all cities."""
        all_cities = data_manager.get_all_cities()
        return all_cities

    @api.expect(city_model)
    @api.response(201, 'City successfully created')
    @api.response(400, 'Invalid request')
    def post(self):
        """Create a new city."""
        new_city_data = request.json
        city_id = data_manager.save_city(new_city_data)
        response_message = {'message': 'City successfully created', 'city_id': city_id}
        return response_message, 201

@api.route('/<string:city_id>')
class CityResource(Resource):
    @api.marshal_with(city_model_extended)
    @api.response(404, 'City not found')
    def get(self, city_id):
        """Retrieve a city by its ID."""
        city_data = data_manager.get_city(city_id)
        if city_data:
            return city_data
        else:
            api.abort(404, "City not found")

    @api.expect(city_model)
    @api.response(204, 'City successfully updated')
    @api.response(400, 'Invalid request')
    @api.response(404, 'City not found')
    def put(self, city_id):
        """Update an existing city."""
        new_city_data = request.json
        updated = data_manager.update_city(city_id, new_city_data)
        if updated:
            return '', 204
        else:
            api.abort(404, "City not found")

    @api.response(204, 'City successfully deleted')
    @api.response(404, 'City not found')
    def delete(self, city_id):
        """Delete an existing city."""
        deleted = data_manager.delete_city(city_id)
        if deleted:
            return '', 204
        else:
            api.abort(404, "City not found")
