
import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config: 
    SECRET_KEY = 'FLASK_BOOKS' 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_TRANSLATION_DIRECTORIES = os.path.join(basedir,'translations')


