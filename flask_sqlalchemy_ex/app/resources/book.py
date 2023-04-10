from flask_restful import Api, Resource 
from app.extensions import db 
from flask import Blueprint, request, jsonify
from app.models.book import Book 


book_bp = Blueprint('book', __name__ ,url_prefix='/book')
api = Api(book_bp)

class BookList(Resource): 
    def get(self): 
        return 'ListBook'
    
    def post(self): 
        data = request.get_json()      
        title = data['title']
        book = Book(title=title) 
        db.session.add(book)
        db.session.commit()  
        return title
    
api.add_resource(BookList, '/') 
