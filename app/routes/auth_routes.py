from flask import Blueprint
from app.controllers.auth_controller import AuthController
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    return AuthController.register()

@auth_bp.route('/login', methods=['POST'])
def login():
    return AuthController.login()

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    return AuthController.refresh()

