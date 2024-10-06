


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from flasgger import Swagger

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)  # Initialize Flask-Migrate with the app and db
    jwt = JWTManager(app)
    Swagger(app)

    # Import routes and blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.blog_routes import blog_bp
    from app.routes.profile_router import profile_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(blog_bp, url_prefix='/api')
    app.register_blueprint(profile_bp, url_prefix='/account')

    return app

