from app.extensions import ma 
from marshmallow import validate, ValidationError, fields
from app.utils import must_not_be_black 

class BookSchema (ma.Schema) : 
    book_name = fields.String(required=True, allow_none=False, validate=must_not_be_black)
    author = fields.String(required=True, allow_none=True)
    genre = fields.String(required=False, allow_none=True)
    users = ma.Nested('UserSchema', many = True )
 
    class Meta: 
       fields = ("book_id","book_name","author", "genre")   

