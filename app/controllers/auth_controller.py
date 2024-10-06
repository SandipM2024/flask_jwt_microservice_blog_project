from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from app.services.auth_service import AuthService
from app.utils.jwt_util import generate_tokens

class AuthController:
    @staticmethod
    def register():
        data = request.get_json()
        username = data['username']
        password = data['password']
        user = AuthService.register(username, password)
        return jsonify({"id": user.id, "username": user.username}), 201

    @staticmethod
    def login():
        data = request.get_json()
        username = data['username']
        password = data['password']
        user = AuthService.authenticate(username, password)
        if user:
            access_token, refresh_token = generate_tokens(user)
            return jsonify(access_token=access_token, refresh_token=refresh_token), 200
        return jsonify({"msg": "Bad username or password"}), 401

    @staticmethod
    @jwt_required(refresh=True)
    def refresh():
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return jsonify(access_token=access_token), 200
