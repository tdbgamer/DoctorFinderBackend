import json

from flask import Blueprint, request, Response
from sqlalchemy import func, and_
from models import Doctor, Address, Rating
from main import db
from utils import ifilter_by

doctors = Blueprint('doctors', __name__)


@doctors.route('/doctors', methods=['POST'])
def make_doctor():
    json_data = request.get_json(force=True)

    doc = Doctor(name=json_data['name'],
                 occupation=json_data['occupation'])
    for address in json_data['addresses']:
        addr = Address(phone_number=address['phone_number'],
                       street_address=address['street_address'],
                       city=address['city'],
                       state=address['state'],
                       zipcode=address['zipcode'],
                       long=address['long'],
                       lat=address['lat'])
        doc.addresses.append(addr)

    db.session.add(doc)
    db.session.commit()

    return Response(status=200)


@doctors.route('/doctors', methods=['GET'])
@doctors.route('/doctors/<int:id>', methods=['GET'])
def get_doctors(id=None):
    query_params = request.args.to_dict()
    if id is not None:
        query_params['id'] = id

    doctors = Doctor.query.filter(ifilter_by(Doctor, **query_params)).all()

    doctor_list = []
    for doctor in doctors:
        doctor_list.append(doctor.serialize(deep=True))
    return Response(json.dumps(doctor_list), content_type='application/json')


@doctors.route('/doctors/<int:id>/ratings', methods=['POST'])
def make_ratings(id):
    json_data = request.get_json(force=True)

    doc = Doctor.query.filter_by(id=id).first()
    if doc is None:
        return Response('Doctor does not exist', status=404)

    doc.ratings.append(Rating(stars=json_data['stars'],
                              username=json_data.get('username', 'Anonymous'),
                              review=json_data['review']))

    db.session.commit()

    return Response(status=200)
