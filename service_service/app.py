from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from config import configurations
from controller.controller import service_blueprint
from model.schemas import ma
from model.serviceType import db


# db = SQLAlchemy()
# ma = Marshmallow()


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(configurations[config_name])
    app.register_blueprint(service_blueprint, url_prefix='/api')

    db.init_app(app)
    ma.init_app(app)
    app.run(host='0.0.0.0', port=5001)
    # with app.app_context():
    #     db.create_all()
    return app
