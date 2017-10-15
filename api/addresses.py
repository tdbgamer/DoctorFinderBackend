import json

from flask import Blueprint, request, Response
from models import Doctor, Address
from main import db

addresses = Blueprint('addresses', __name__)

@addresses.route('/addresses', methods=['GET'])
@addresses.route('/addresses/<int:id>', methods=['GET'])
def get_addresses(id=None):
    query_params = request.args.to_dict()
    if id is not None:
        query_params['id'] = id
    addresses = Address.query.filter_by(**query_params).all()

    addresses_list = []
    for address in addresses:
        addresses_list.append(address.serialize(deep=True))

    return Response(json.dumps(addresses_list), content_type='application/json')
