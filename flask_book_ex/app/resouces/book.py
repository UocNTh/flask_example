from flask import jsonify, request, Blueprint
from flask_restful import Resource, Api 
from flask_babel import _ 
from app.extensions import db 
from marshmallow import ValidationError
from app.models.book import Book 
from app.schema.user import UserSchema 
from app.schema.book import BookSchema


book_bp = Blueprint('book', __name__ , url_prefix='/books')
api = Api(book_bp) 

user_schema = UserSchema() 
users_schema = UserSchema(many = True)
book_schema = BookSchema() 
books_schema = BookSchema(many = True) 

class BookList(Resource) : 
    def get (self): 
        books = Book.query.all() 
        if not books : 
            return jsonify({'message':_('No books')})
        return jsonify(books_schema.dump(books))
    
    def post(self): 
        data = request.get_json() 

        book_name = data['book_name'] 
        author = data['author'] 
        genre = data["genre"] 

        error = book_schema.validate({
            "book_name" : book_name ,
            "author" : author ,
            "genre" : genre ,
        })

        if error:
            return jsonify(error) 
        
        new_book = Book(book_name = book_name ,
                        author = author,
                        genre = genre 
                        ) 

        try:
            result = book_schema.load(data)
        except ValidationError as err:
            return err.messages, 422
        
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'message': _('New book has been created')})

class BookByID (Resource): 
    def get(self, id): 
        book = Book.query.get(id) 
        if not book : 
            return jsonify({'message':_('Not fould book')})
        return jsonify(book_schema.dump(book))
    
    def delete(self,id):
        book = Book.query.get(int(id) ) 
        if not book : 
            return jsonify({'message':_('Not fould book')})
        db.session.delete(book) 
        db.session.commit() 
        return jsonify({'message': _('The book has been deleted')})
    
    def put(self, id): 
        book = Book.query.get(id)
        if not book : 
            return jsonify({'message':_('Not fould book')})
        
        data = request.get_json() 

        book_name = data['book_name'] 
        author = data['author'] 
        genre = data["genre"]  

        error = book_schema.validate({
            "book_name" : book_name ,
            "author" : author ,
            "genre" : genre 
        })
        
        if error: 
            return jsonify({"message": error}) 
        
        book.book_name = data['book_name'] 
        book.author = data['author'] 
        book.genre = data["genre"]

        try: 
            result = book_schema.load(data) 
        except ValidationError as err : 
            return {"errors": err.messages}, 422

        db.session.commit()
        return jsonify({'message' : _('The changes have been saved')})
    
class BookOrder(Resource):
    def get(self, book_id) : 
        book = Book.query.get(book_id) 
        if not book: 
            return jsonify({'message':_('Not fould book')})
        book_users = book.users 

        return jsonify(users_schema.dump(book_users)) 
    
api.add_resource(BookList, '/')
api.add_resource(BookByID, '/<int:id>')
api.add_resource(BookOrder,'/<int:book_id>/users') 