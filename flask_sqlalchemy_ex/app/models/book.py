from app.extensions import db 

class Book(db.Model) : 
    id = db.Column(db.Integer, primary_key = True) 
    title = db.Column(db.String(100)) 