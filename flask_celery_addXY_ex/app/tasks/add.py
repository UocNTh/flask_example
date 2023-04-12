from app.extensions import celery

@celery.task 
def add_xy(x,y): 
    return x+y 