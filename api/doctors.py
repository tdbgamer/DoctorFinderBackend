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
