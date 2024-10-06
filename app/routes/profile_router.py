from flask import Blueprint

from app.controllers.profile_controller import ProfileController


profile_bp = Blueprint('profile', __name__)



# Profile routes
@profile_bp.route('/profile', methods=['GET'])

def get_profile():
    return ProfileController.get_profile()

@profile_bp.route('/profile/update', methods=['PUT'])
def update_profile():
    return ProfileController.update_profile()


