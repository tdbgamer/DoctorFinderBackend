import json

from flask import Blueprint, request, Response
from models import Doctor, Address
from main import db

addresses = Blueprint('addresses', __name__)

@addresses.route('/addresses', methods=['GET'])
def get_addresses():
    query_params = request.args.to_dict()
    addresses = Address.query.filter_by(**query_params).all()

    addresses_list = []
    for address in addresses:
        addresses_list.append(address.serialize(deep=True))

    return Response(json.dumps(addresses_list), content_type='application/json')
