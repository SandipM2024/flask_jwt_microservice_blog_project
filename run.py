# from app import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from app import create_app

app = create_app()

# SWAGGER_URL = '/swagger'
# API_URL = '/static/swagger.json'  # Path to your swagger.json file
# swaggerui_blueprint = get_swaggerui_blueprint(
#     SWAGGER_URL,
#     API_URL,
#     config={
#         'app_name': "Flask JWT Microservice"
#     }
# )
# app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)

