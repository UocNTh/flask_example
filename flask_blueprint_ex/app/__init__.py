from flask import Flask 
from app.extensions import api 
from app.resources.home import home_bp

def create_app() : 
    app = Flask(__name__) 

    api.init_app(app) 

    app.register_blueprint(home_bp) 

    return app 




