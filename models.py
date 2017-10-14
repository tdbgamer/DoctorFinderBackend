from main import db

doctor_address = db.Table('doctor_address',
    db.Column('doctor_id', db.Integer, db.ForeignKey('doctor.id')),
    db.Column('address_id', db.Integer, db.ForeignKey('address.id'))
)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)
    addresses = db.relationship('Address', secondary=doctor_address,
                                lazy='subquery', backref=db.backref('doctors', lazy='joined'))

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street_address = db.Column(db.String)
    zipcode = db.Column(db.Integer)
    phone_number = db.Column(db.Integer)
    long = db.Column(db.Float)
    lat = db.Column(db.Float)

if __name__ == '__main__':
    db.create_all()
