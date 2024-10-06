from flask import Blueprint
from app.controllers.blog_controller import BlogController

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/blogs', methods=['POST'])
def create_blog():
    return BlogController.create_blog()

@blog_bp.route('/blogs', methods=['GET'])
def get_all_blogs():
    return BlogController.get_all_blogs()

@blog_bp.route('/blogs/<int:blog_id>', methods=['GET'])
def get_blog(blog_id):
    return BlogController.get_blog(blog_id)

@blog_bp.route('/blogs/<int:blog_id>', methods=['PUT'])
def update_blog(blog_id):
    return BlogController.update_blog(blog_id)

@blog_bp.route('/blogs/<int:blog_id>', methods=['DELETE'])
def delete_blog(blog_id):
    return BlogController.delete_blog(blog_id)
