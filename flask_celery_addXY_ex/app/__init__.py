from flask import Flask
from app.extensions import celery, init_celery
from config import Config
from app.resources.home import home_bp
from app.resources.add import add_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_celery(app)

    app.register_blueprint(home_bp)
    app.register_blueprint(add_bp)

    return app

