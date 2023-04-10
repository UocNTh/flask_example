from flask import Flask , request, jsonify
from celery import Celery
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
db = SQLAlchemy() 
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'db+sqlite:///flask_book.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_book.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db.init_app(app)
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'], backend=app.config['CELERY_RESULT_BACKEND'])
 
class Book(db.Model) : 
    id = db.Column(db.Integer, primary_key = True, autoincrement = True ) 
    title = db.Column(db.String(100))


with app.app_context(): 
    db.create_all()

@celery.task
def add(title): 
    with app.app_context():
        book = Book(title=title) 
        db.session.add(book) 
        db.session.commit()
        return 'Done'

@app.route('/add', methods = ['POST'])
def add_book(): 
    data = request.get_json() 
    title = data['title']
    result = add.delay(title) 
    return jsonify({'id': result.id, 'status': result.status})


if __name__ == "__main__" : 
    app.run(debug =True) 