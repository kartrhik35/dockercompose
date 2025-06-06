# app/__init__.py
from flask import Flask
from app.cache import cache

def create_app():
    app = Flask(__name__)
    cache.init_app(app)

    @app.route("/")
    def home():
        count = cache.incr("hits")
        return f"You've visited {count} times."

    return app
