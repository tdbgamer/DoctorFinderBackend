from flask import current_app
from flask_migrate import MigrateCommand
from main import manager
import csv

if __name__ == '__main__':
    from models import *

    manager.add_command('db', MigrateCommand)

    @manager.command
    def insert_data():
        from main import make_app, db
        app = make_app()
        with app.app_context():
            with open('fake_data.csv', 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    doctor = Doctor(name=row['name'], occupation=row['occupation'])
                    address = Address(phone_number=int(row['phone_number']),
                                      street_address=row['street_address'],
                                      city=row['city'],
                                      state=row['state'],
                                      zipcode=int(row['zipcode']),
                                      long=float(row['long']),
                                      lat=float(row['lat']))
                    doctor.addresses.append(address)

                    db.session.add(doctor)
                db.session.commit()

    manager.run()
