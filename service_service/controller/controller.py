from flask import Blueprint, jsonify, request

from model.serviceType import ServiceType
from model.schemas import ServiceTypeSchema

from model.serviceType import db

service_blueprint = Blueprint('service', __name__)
service_type_schema = ServiceTypeSchema()


@service_blueprint.route('/services', methods=['GET'])
def get_services():
    try:
        service_types = ServiceType.query.all()
        return jsonify({'services': service_type_schema.dump(service_types, many=True)})
    except Exception as e:
        print("Exception:", e)
        return jsonify({"error": "Internal Server Error"}), 500


@service_blueprint.route('/services', methods=['POST'])
def create_service():
    data = request.get_json()
    new_service = ServiceType(
        service_name=data.get('service_name'),
        description=data.get('description'),
        price=data.get('price')
    )
    db.session.add(new_service)
    db.session.commit()
    return jsonify(
        {'message': 'tipo de servico criado com sucesso', 'service': service_type_schema.dump(new_service)}), 201


@service_blueprint.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    service_type = ServiceType.query.get(service_id)
    if service_type:
        return jsonify({'service': service_type_schema.dump(service_type)})
    else:
        return jsonify({'message': 'Tipo de serviço não encontrado'}), 404


# @service_blueprint.route('/services', methods=['POST'])
# def create_service():
#     data = request.get_json()
#     new_service_type = ServiceType(name=data['name'], description=data.get('description', ''))
#     db.session.add(new_service_type)
#     db.session.commit()
#     return jsonify({'message': 'Tipo de serviço criado com sucesso', 'service': service_type_schema.dump(new_service_type)}), 201

@service_blueprint.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    service_type = ServiceType.query.get(service_id)
    if service_type:
        data = request.get_json()
        service_type.name = data['name']
        service_type.description = data.get('description', '')
        db.session.commit()
        return jsonify(
            {'message': 'Tipo de serviço atualizado com sucesso', 'service': service_type_schema.dump(service_type)})
    else:
        return jsonify({'message': 'Tipo de serviço não encontrado'}), 404


@service_blueprint.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    service_type = ServiceType.query.get(service_id)
    if service_type:
        db.session.delete(service_type)
        db.session.commit()
        return jsonify({'message': 'Tipo de serviço excluído com sucesso'})
    else:
        return jsonify({'message': 'Tipo de serviço não encontrado'}), 404
