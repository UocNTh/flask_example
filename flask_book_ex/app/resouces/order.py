from flask_restful import Resource, Api 
from flask import request, jsonify, Blueprint
from app.models.user import User
from app.models.book import Book
from flask_babel import _
from app.extensions import db

order_bp = Blueprint('order', __name__ , url_prefix= '/orders')
api = Api(order_bp)
class Order(Resource): 
    def post(self): 
        data = request.get_json() 
        user_id = data['user_id'] 
        book_id = data['book_id'] 
        user = User.query.get(user_id) 
        if not user: 
            return jsonify({'message':_('Not fould user')})
        book = Book.query.get(book_id)
        if not book : 
            return jsonify({'message':_('Not fould book')})
        user.books.append(book) 
        db.session.commit() 
        return jsonify({'message':_('Successed')})

api.add_resource(Order, '/') 
