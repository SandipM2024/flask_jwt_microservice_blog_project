from app.models.blog import Blog
from app import db

class BlogService:
    @staticmethod
    def create_blog(title, content, author_id):
        new_blog = Blog(title=title, content=content, author_id=author_id)
        db.session.add(new_blog)
        db.session.commit()
        return new_blog

    @staticmethod
    def get_all_blogs():
        return Blog.query.all()

    @staticmethod
    def get_blog(blog_id):
        return Blog.query.get(blog_id)

    @staticmethod
    def update_blog(blog_id, title, content):
        blog = Blog.query.get(blog_id)
        if blog:
            blog.title = title
            blog.content = content
            db.session.commit()
            return blog
        return None

    @staticmethod
    def delete_blog(blog_id):
        blog = Blog.query.get(blog_id)
        if blog:
            db.session.delete(blog)
            db.session.commit()
            return True
        return False
