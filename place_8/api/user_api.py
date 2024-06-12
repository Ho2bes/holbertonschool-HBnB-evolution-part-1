#!/usr/bin/python3


# API for managing users
from flask import request
from flask_restx import Namespace, Resource, fields
from data_manager import DataManager

api = Namespace('users', description='Users related operations')
data_manager = DataManager()

# Data model for creating a user
user_model = api.model('User', {
    'username': fields.String(required=True, description='Username'),
    'email': fields.String(required=True, description='Email'),
    'password': fields.String(required=True, description='Password')
})

# Route for managing users
@api.route('/')
class Users(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        """Fetches all users."""
        return data_manager.get_all_users()

    @api.expect(user_model)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Invalid request')
    def post(self):
        """Creates a new user."""
        new_user_data = request.json
        user_id = data_manager.save_user(new_user_data)
        response = {'message': 'User successfully created', 'user_id': user_id}
        return response, 201

@api.route('/<string:user_id>')
class UserResource(Resource):
    @api.marshal_with(user_model)
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Fetches a user by their ID."""
        user = data_manager.get_user(user_id)
        if user:
            return user
        else:
            api.abort(404, "User not found")

    @api.response(204, 'User successfully deleted')
    @api.response(404, 'User not found')
    def delete(self, user_id):
        """Deletes an existing user."""
        deleted = data_manager.delete_user(user_id)
        if deleted:
            return '', 204
        else:
            api.abort(404, "User not found")

    @api.expect(user_model)
    @api.response(204, 'User successfully updated')
    @api.response(400, 'Invalid request')
    @api.response(404, 'User not found')
    def put(self, user_id):
        """Updates an existing user."""
        new_user_data = request.json
        updated = data_manager.update_user(user_id, new_user_data)
        if updated:
            return '', 204
        else:
            api.abort(404, "User not found")
