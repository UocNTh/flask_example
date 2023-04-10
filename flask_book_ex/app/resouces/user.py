from flask import jsonify, request, Blueprint
from flask_restful import Resource , Api 
from app.models.user import User
from app.schema.user import UserSchema
from app.schema.book import BookSchema 
from app.extensions import db
from marshmallow import ValidationError
from flask_babel import _

user_bp = Blueprint('user', __name__ , url_prefix= '/users')
api = Api(user_bp)

user_schema = UserSchema() 
users_schema = UserSchema(many = True)
book_schema = BookSchema() 
books_schema = BookSchema(many = True) k

class UserList(Resource) : 
    def get (self): 
        users = User.query.all() k
        if not users : 
            return jsonify({'message': _('No users')})
        return jsonify(users_schema.dump(users))
    
    def post(self): k
        data = request.get_json() 

        user_name = data['user_name'] 
        address = data['address'] 
        phone_number = data['phone_number']
        email = data["email"] 

        error = user_schema.validate({
            "user_name" : user_name ,
            "address" : address ,
            "phone_number" : phone_number ,
            "email" : email ,
        })

        if error:
            return jsonify(error) 
        
        new_user = User(user_name = user_name ,
                        address = address,
                        phone_number = phone_number,
                        email = email 
                        ) 

        try:
            result = user_schema.load(data)
        except ValidationError as err:
            return err.messages, 422
        
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': _('New user has been created')})

class UserByID (Resource): 
    def get(self, id): 
        user = User.query.get(id) 
        if not user : 
            return jsonify({'message':_('Not fould user')})
        return jsonify(user_schema.dump(user))
    
    def delete(self,id):
        user = User.query.get(int(id) ) 
        if not user : 
            return jsonify({'message':_('Not fould user')})
        db.session.delete(user) 
        db.session.commit() 
        return jsonify({'message': _('The user has been deleted')})
    
    def put(self, id): 
        user = User.query.get(id)
        if not user : 
            return jsonify({'message':_('Not fould user')})
        
        data = request.get_json() 

        user_name = data['user_name'] 
        address = data['address'] 
        phone_number = data['phone_number']
        email = data["email"] 

        error = user_schema.validate({
            "user_name" : user_name ,
            "address" : address ,
            "phone_number" : phone_number ,
            "email" : email 
        })
        
        if error: 
            return jsonify({"message": error}) 
        
        user.user_name = data['user_name']
        user.address = data['address']
        user.phone_number = data['phone_number']
        user.email = data['email']

        try: 
            result = user_schema.load(data) 
        except ValidationError as err : 
            return {"errors": err.messages}

        db.session.commit()
        return jsonify({'message' : _('The changes have been saved')})
    
class UserOrder(Resource):
    def get(self, user_id) : 
        user = User.query.get(user_id) 
        if not user: 
            return jsonify({'message':_('Not fould user')})
        user_books = user.books 

        return jsonify(books_schema.dump(user_books)) 
    
api.add_resource(UserList, '/') 
api.add_resource(UserByID, '/<int:id>')
api.add_resource(UserOrder, '/<int:user_id>/books')