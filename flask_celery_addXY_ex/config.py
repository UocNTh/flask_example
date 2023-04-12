class Config:
    # Flask
    DEBUG = False
    TESTING = False
    SECRET_KEY = "secret"

    # Celery
    CELERY_BROKER_URL = "amqp://localhost/"