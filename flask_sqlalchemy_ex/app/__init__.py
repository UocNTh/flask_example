from flask import Flask
from config import Config
from app.extensions import db, api
from app.resources.book import book_bp

def create_app(config_class = Config): 

    app = Flask(__name__) 
    app.config.from_object(config_class) 
    
    db.init_app(app) 
    api.init_app(app)


    app.register_blueprint(book_bp)

    return app 
