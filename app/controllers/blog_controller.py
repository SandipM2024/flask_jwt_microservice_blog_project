from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.blog_service import BlogService

class BlogController:
    @staticmethod
    @jwt_required()
    def create_blog():
        data = request.get_json()
        title = data['title']
        content = data['content']
        author_id = get_jwt_identity()
        blog = BlogService.create_blog(title, content, author_id)
        return jsonify(blog.to_dict()), 201

    @staticmethod
    @jwt_required()
    def get_all_blogs():
        blogs = BlogService.get_all_blogs()
        return jsonify([blog.to_dict() for blog in blogs]), 200

    @staticmethod
    @jwt_required()
    def get_blog(blog_id):
        blog = BlogService.get_blog(blog_id)
        if blog:
            return jsonify(blog.to_dict()), 200
        return jsonify({"msg": "Blog not found"}), 404

    @staticmethod
    @jwt_required()
    def update_blog(blog_id):
        data = request.get_json()
        title = data['title']
        content = data['content']
        blog = BlogService.update_blog(blog_id, title, content)
        if blog:
            return jsonify(blog.to_dict()), 200
        return jsonify({"msg": "Blog not found"}), 404

    @staticmethod
    @jwt_required()
    def delete_blog(blog_id):
        success = BlogService.delete_blog(blog_id)
        if success:
            return jsonify({"msg": "Blog deleted"}), 200
        return jsonify({"msg": "Blog not found"}), 404
