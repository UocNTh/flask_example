from app.extensions import db 

class User(db.Model): 
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement = True )
    user_name = db.Column(db.String(50), nullable = False )
    address = db.Column(db.String(80))
    phone_number = db.Column(db.String(12))
    email = db.Column(db.String(100))
   
    def __init__ (self, user_name, address , phone_number , email ) : 
        self.user_name = user_name 
        self.address = address 
        self.phone_number = phone_number 
        self.email = email  