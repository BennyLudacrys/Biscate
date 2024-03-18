from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ServiceType(db.Model):
    __tablename__ = "service-type"
    id = db.Column(db.Integer, primary_key=True)
    # provider_id = db.Column(db.integer, db.Foreign_key('users.id'), nullable=True)
    service_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    # provider = db.relationship('User', backref='services')
