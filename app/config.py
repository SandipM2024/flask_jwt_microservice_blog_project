import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'secret_key_rururufjfjffj55757474fjjfj484884')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {
        'title': 'Flask JWT API',
        'uiversion': 3
    }

