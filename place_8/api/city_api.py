#!/usr/bin/python3

# API for managing cities
from flask import request
from flask_restx import Namespace, Resource, fields
from data_manager import DataManager

api = Namespace('cities', description='Cities related operations')
data_manager = DataManager()

# Data model for creating a city
city_model = api.model('City', {
    'name': fields.String(required=True, description='Name of the city'),
    'country_id': fields.String(description='ID of the country', required=True)
})

# Route for managing cities
@api.route('/')
class Cities(Resource):
    @api.marshal_list_with(city_model)
    def get(self):
        """Fetches all cities."""
        return data_manager.get_all_cities()

    @api.expect(city_model)
    @api.response(201, 'City successfully created')
    @api.response(400, 'Invalid request')
    def post(self):
        """Creates a new city."""
        new_city_data = request.json
        city_id = data_manager.save_city(new_city_data)
        response = {'message': 'City successfully created', 'city_id': city_id}
        return response, 201

@api.route('/<string:city_id>')
class CityResource(Resource):
    @api.marshal_with(city_model)
    @api.response(404, 'City not found')
    def get(self, city_id):
        """Fetches a city by its ID."""
        city = data_manager.get_city(city_id)
        if city:
            return city
        else:
            api.abort(404, "City not found")

    @api.response(204, 'City successfully deleted')
    @api.response(404, 'City not found')
    def delete(self, city_id):
        """Deletes an existing city."""
        deleted = data_manager.delete_city(city_id)
        if deleted:
            return '', 204
        else:
            api.abort(404, "City not found")

    @api.expect(city_model)
    @api.response(204, 'City successfully updated')
    @api.response(400, 'Invalid request')
    @api.response(404, 'City not found')
    def put(self, city_id):
        """Updates an existing city."""
        new_city_data = request.json
        updated = data_manager.update_city(city_id, new_city_data)
        if updated:
            return '', 204
        else:
            api.abort(404, "City not found")
