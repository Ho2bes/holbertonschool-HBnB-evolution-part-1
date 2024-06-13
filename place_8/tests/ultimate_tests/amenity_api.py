from flask import Blueprint, request
from flask_restx import Api, Resource, fields
from model.amenity import Amenity
from persistence.amenity_repository import AmenityRepository

# Create a blueprint for the amenity API
amenity_blueprint = Blueprint('amenity_api', __name__)
api = Api(amenity_blueprint)

amenity_repository = AmenityRepository()

# Define the amenity model
amenity_model = api.model('Amenity', {
    'amenity_id': fields.String(readOnly=True, description='The unique identifier of an amenity'),
    'name': fields.String(required=True, description='Amenity name'),
    'created_at': fields.DateTime(readOnly=True, description='The time the amenity was created'),
    'updated_at': fields.DateTime(readOnly=True, description='The time the amenity was last updated')
})

@api.route('/amenities')
class AmenityList(Resource):
    @api.marshal_list_with(amenity_model)
    def get(self):
        """List all amenities"""
        return amenity_repository.get_all()

    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created.')
    def post(self):
        """Create a new amenity"""
        data = request.json
        amenity = Amenity(**data)
        amenity_id = amenity_repository.save(amenity)
        return {'amenity_id': amenity_id}, 201

@api.route('/amenities/<string:amenity_id>')
@api.response(404, 'Amenity not found.')
class AmenityResource(Resource):
    @api.marshal_with(amenity_model)
    def get(self, amenity_id):
        """Fetch an amenity by its ID"""
        amenity = amenity_repository.get(amenity_id)
        if amenity:
            return amenity
        api.abort(404, 'Amenity not found.')

    @api.expect(amenity_model)
    @api.response(204, 'Amenity successfully updated.')
    def put(self, amenity_id):
        """Update an amenity by its ID"""
        data = request.json
        updated = amenity_repository.update(amenity_id, data)
        if updated:
            return '', 204
        api.abort(404, 'Amenity not found.')

    @api.response(204, 'Amenity successfully deleted.')
    def delete(self, amenity_id):
        """Delete an amenity by its ID"""
        deleted = amenity_repository.delete(amenity_id)
        if deleted:
            return '', 204
        api.abort(404, 'Amenity not found.')
