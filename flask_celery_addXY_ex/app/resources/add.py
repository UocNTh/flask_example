from app.tasks.add import add_xy 
from flask import Blueprint, request

add_bp = Blueprint('add', __name__,url_prefix='/add')


@add_bp.route('/', methods = ['POST'])
def add(): 
    data = request.get_json() 
    x = data['x'] 
    y = data['y'] 

    result = add_xy.delay(x,y) 

    return {'task_id': result.id }