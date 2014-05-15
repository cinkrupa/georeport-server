__author__ = 'Marcin'

from app import db, model
from data import srs

#app.test_request_context().push()
db.create_all()
user = model.User("mkrupa", "mkrupa@student.agh.edu.pl")
db.session.add(user)
db.session.commit()
for request_data in srs:
    request = model.ServiceRequest()
    request.id = request_data['service_request_id']
    if request_data['status'] == 'closed':
        request.status = 1
    else:
        request.status = 0
    request.status_notes = request_data['status_notes']
    request.service_name = request_data['service_name']
    request.service_code = request_data['service_code']
    request.description = request_data['description']
    request.agency_responsible = request_data['agency_responsible']
    request.service_notice = request_data['service_notice']
    #request.requested_datetime = request_data['requested_datetime']
    #request.updated_datetime = request_data['updated_datetime']
    #request.expected_datetime = request_data['expected_datetime']
    request.address = request_data['address']
    request.address_id = request_data['address_id']
    request.zipcode = request_data['zipcode']
    request.lat = request_data['lat']
    request.long = request_data['long']
    request.media_url = request_data['media_url']
    db.session.add(request)
    db.session.commit()



