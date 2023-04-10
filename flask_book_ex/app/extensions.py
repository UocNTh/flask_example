rom flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_babel import Babel, _ 
from app.utils import get_locale 

db = SQLAlchemy() 
ma = Marshmallow()
api = Api()
# babel = Babel(locale_selector = get_locale) 

