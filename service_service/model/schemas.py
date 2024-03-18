from flask_marshmallow import Marshmallow


ma = Marshmallow()


class ServiceTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ('id', 'service_name', 'description', 'price')

