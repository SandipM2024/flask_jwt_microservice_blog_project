from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from app import db

class ProfileController:
    @staticmethod
    @jwt_required()
    def get_profile():
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if user:
            return jsonify({"id": user.id, "username": user.username}), 200
        return jsonify({"msg": "User not found"}), 404

    @staticmethod
    @jwt_required()
    def update_profile():
        user_id = get_jwt_identity()
        data = request.get_json()
        user = User.query.get(user_id)

        if user:
            user.username = data.get('username', user.username)
            db.session.commit()
            return jsonify({"msg": "Profile updated successfully"}), 200
        return jsonify({"msg": "User not found"}), 404
