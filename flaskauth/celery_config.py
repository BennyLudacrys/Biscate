from celery import Celery
from flask import Flask

app = Flask(__name__)

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6380/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6380/0'

celery = Celery(app.import_name,
                backend=app.config['CELERY_RESULT_BACKEND'],
                broker=app.config['CELERY_BROKER_URL'])

celery.conf.update(app.config)
