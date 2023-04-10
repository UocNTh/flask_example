from flask import Flask, request
from config import Config
from flask_babel import Babel
from app.extensions import db, ma , api
from .resouces.book import book_bp 
from .resouces.user import user_bp
from .resouces.order import order_bp
def create_app(config_class = Config) : 
    app = Flask(__name__) 
    app.config.from_object(config_class)

    # khai bao cac tien ich mo rong
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)

    def get_locale(): 
        return request.accept_languages.best_match(['en', 'vi']) 
    
    babel = Babel(app, locale_selector = get_locale )


    app.register_blueprint(book_bp) 
    app.register_blueprint(user_bp)
    app.register_blueprint(order_bp)

    @app.route('/') 
    def home() : 
        return 'Home'
    return app 
