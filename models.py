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

    def serialize(self):
        return {
            "name": self.name,
            "occupation": self.occupation,
        }

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Float)
    username = db.Column(db.String, default='Anonymous')
    review = db.Column(db.String)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'),
                          nullable=False)

    def serialize(self):
        return {
            "stars": self.stars,
            "username": self.username,
            "review": self.review
        }

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street_address = db.Column(db.String)
    zipcode = db.Column(db.Integer)
    phone_number = db.Column(db.BigInteger)
    long = db.Column(db.Float)
    lat = db.Column(db.Float)

    def serialize(self):
        return {
            "phone_number": self.phone_number,
            "street_address": self.street_address,
            "zipcode": self.zipcode,
            "long": self.long,
            "lat": self.lat
        }

if __name__ == '__main__':
    db.create_all()
