from flask_jwt_extended import JWTManager
from app import app

jwt = JWTManager(app)

@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return {'msg': 'Missing Authorization Header'}, 401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return {'msg': 'Token has expired'}, 401
