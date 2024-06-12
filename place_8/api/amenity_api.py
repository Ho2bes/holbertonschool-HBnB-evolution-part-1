#!/usr/bin/python3

# API for managing amenities
from flask import request
from flask_restx import Namespace, Resource, fields
from data_manager import DataManager

api = Namespace('amenities', description='Amenities related operations')
data_manager = DataManager()

# Data model for creating an amenity
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

# Route for managing amenities
@api.route('/')
class Amenities(Resource):
    @api.marshal_list_with(amenity_model)
    def get(self):
        """Fetches all amenities."""
        return data_manager.get_all_amenities()

    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid request')
    def post(self):
        """Creates a new amenity."""
        new_amenity_data = request.json
        amenity_id = data_manager.save_amenity(new_amenity_data)
        response = {'message': 'Amenity successfully created', 'amenity_id': amenity_id}
        return response, 201

@api.route('/<string:amenity_id>')
class AmenityResource(Resource):
    @api.marshal_with(amenity_model)
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Fetches an amenity by its ID."""
        amenity = data_manager.get_amenity(amenity_id)
        if amenity:
            return amenity
        else:
            api.abort(404, "Amenity not found")

    @api.response(204, 'Amenity successfully deleted')
    @api.response(404, 'Amenity not found')
    def delete(self, amenity_id):
        """Deletes an existing amenity."""
        deleted = data_manager.delete_amenity(amenity_id)
        if deleted:
            return '', 204
        else:
            api.abort(404, "Amenity not found")

    @api.expect(amenity_model)
    @api.response(204, 'Amenity successfully updated')
    @api.response(400, 'Invalid request')
    @api.response(404, 'Amenity not found')
    def put(self, amenity_id):
        """Updates an existing amenity."""
        new_amenity_data = request.json
        updated = data_manager.update_amenity(amenity_id, new_amenity_data)
        if updated:
            return '', 204
        else:
            api.abort(404, "Amenity not found")
