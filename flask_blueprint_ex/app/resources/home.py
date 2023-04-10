from flask_restful import Resource , Api 
from flask import Blueprint 


home_bp = Blueprint('home', __name__, url_prefix='/')
api = Api(home_bp)

class Hello(Resource): 
    def get(self):
        return 'Home'
    
api.add_resource(Hello, '/home') 