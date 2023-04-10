from app.extensions import db 


user_book = db.Table('user_book',
                     db.Column('book_id', db.Integer, db.ForeignKey('books.book_id')),
                     db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'))
                     )

class Book(db.Model) : 
    __tablename__ = "books" 
    book_id = db.Column(db.Integer, primary_key=True, autoincrement = True )
    book_name = db.Column(db.String(50), nullable = False )
    author = db.Column(db.String(50), nullable = False ) 
    genre= db.Column(db.String(100)) 
    users = db.relationship('User', secondary = user_book, backref = 'books') 

    def __init__ (self, book_name, author , genre ) : 
        self.book_name = book_name 
        self.author = author 
        self.genre = genre 

