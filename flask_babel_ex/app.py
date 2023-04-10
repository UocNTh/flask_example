from flask import Flask, request 
from flask_babel import Babel, _ 

app = Flask(__name__) 

def get_locale() : 
    return request.accept_languages.best_match(['en', 'vi', 'fr']) 

babel = Babel(app, locale_selector = get_locale) 

@app.route('/')
def home() : 
    return _('Home') 

if __name__ == "__main__" : 
    app.run(debug = True ) 