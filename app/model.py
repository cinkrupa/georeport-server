__author__ = 'Marcin'

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean)
    status_notes = db.Column(db.String(50))
    service_name = db.Column(db.String(50))
    service_code = db.Column(db.Integer)
    description = db.Column(db.String(160))
    agency_responsible = db.Column(db.String(50))
    service_notice = db.Column(db.String(80))
    requested_datetime = db.Column(db.DateTime)
    updated_datetimec = db.Column(db.DateTime)
    expected_datetime = db.Column(db.DateTime)
    address = db.Column(db.String(80))
    address_id = db.Column(db.Integer)
    zipcode = db.Column(db.Integer)
    lat = db.Column(db.Float)
    long = db.Column(db.Float)
    media_url = db.Column(db.String(80))

    def __repr__(self):
        return '<ServiceRequest %r>' % self.id