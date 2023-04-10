from app.extensions import ma 
from marshmallow import validate, ValidationError, fields , validates
from app.utils import must_not_be_black 
from flask_babel import _ 

class UserSchema (ma.Schema) : 
    user_name = fields.String(required=True, allow_none=False,validate = must_not_be_black ) 
    address = fields.String(required=False, allow_none=True)
    phone_number = fields.String(required=False, allow_none = True, validate=validate.Length(min=10, max =12))
    email = fields.String(required=False, allow_none=True)
    books = ma.Nested('BookSchema', many = True )
    @validates('email') 
    def validate_email(self, email): 
        if not email.endswith('@gmail.com'):
            raise ValidationError(_('Email must end with @gmail.com'))
    class Meta: 
        fields = ("user_id", "user_name", "address", "phone_number", "email") 

