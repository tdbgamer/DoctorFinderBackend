import json

from flask import Blueprint, request, Response
from models import Doctor, Address
from main import db

doctors = Blueprint('doctors', __name__)

@doctors.route('/doctors', methods=['POST'])
def make_doctor():
    json_data = request.get_json(force=True)

    doc = Doctor(name=json_data['name'],
                 occupation=json_data['occupation'])
    for address in json_data['addresses']:
        addr = Address(phone_number=address['phone_number'],
                       street_address=address['street_address'],
                       zipcode=address['zipcode'],
                       long=address['long'],
                       lat=address['lat'])
        doc.addresses.append(addr)

    db.session.add(doc)
    db.session.commit()

    return Response(status=200)

@doctors.route('/doctors', methods=['GET'])
def get_doctors():
    doctors = Doctor.query.all()
    doctor_list = []
    for doctor in doctors:
        doc = doctor.serialize()
        doc['addresses'] = []
        for address in doctor.addresses:
            doc['addresses'].append(address.serialize())
        doctor_list.append(doc)
    return Response(json.dumps(doctor_list), content_type='application/json')
