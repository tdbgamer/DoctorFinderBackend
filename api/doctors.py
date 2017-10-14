import json

from flask import Blueprint, request, Response
from models import Doctor
from main import db

doctors = Blueprint('doctors', __name__)

@doctors.route('/doctors', methods=['POST'])
def make_doctor():
    json_data = request.get_json(force=True)

    doc = Doctor(name=json_data['name'],
                 occupation=json_data['occupation'])

    db.session.add(doc)
    db.session.commit()

    return Response(status=200)


@doctors.route('/doctors', methods=['GET'])
def get_doctors():
    doctors = Doctor.query.all()
    doctor_list = []
    for doctor in doctors:
        doctor_list.append({
            "name": doctor.name,
            "occupation": doctor.occupation
        })
    return Response(json.dumps(doctor_list), content_type='application/json')
