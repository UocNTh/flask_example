from flask import request 
from  marshmallow import ValidationError 
from flask_babel import _

def must_not_be_black(data) : 
    if not data : 
        return ValidationError(_('Data not provided'))
    

def get_locale(): 
    return request.accept_languages.best_match(['en', 'vi']) 
