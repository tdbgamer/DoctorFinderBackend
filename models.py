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
    ratings = db.relationship('Rating', backref='doctor', lazy=True)

    def serialize(self, deep=False):
        doctor = {"id": self.id,
                  "name": self.name,
                  "occupation": self.occupation,
                  "ratings": []}

        for rating in self.ratings:
            doctor['ratings'].append(rating.serialize())

        if deep:
            doctor['addresses'] = []
            for address in self.addresses:
                doctor['addresses'].append(address.serialize())

        return doctor

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Float)
    username = db.Column(db.String, default='Anonymous')
    review = db.Column(db.String)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'),
                          nullable=False)

    def serialize(self):
        return {"id": self.id,
                "stars": self.stars,
                "username": self.username,
                "review": self.review}

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street_address = db.Column(db.String)
    state = db.Column(db.String)
    city = db.Column(db.String)
    zipcode = db.Column(db.Integer)
    phone_number = db.Column(db.BigInteger)
    long = db.Column(db.Float)
    lat = db.Column(db.Float)

    def serialize(self, deep=False):
        address = {"id": self.id,
                   "phone_number": self.phone_number,
                   "street_address": self.street_address,
                   "city": self.city,
                   "state": self.state,
                   "zipcode": self.zipcode,
                   "long": self.long,
                   "lat": self.lat}
        if deep:
            address['doctors'] = []
            for doctor in self.doctors:
                address['doctors'].append(doctor.serialize())
        return address

if __name__ == '__main__':
    db.create_all()
