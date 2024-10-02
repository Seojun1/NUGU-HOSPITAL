from flask import request, g, Blueprint
from flask_restx import Resource, Api
import requests
from utils import create_message_location, location_hospital

class locationAction(Resource):
    def post(self):
        data = request.get_json()
        action = data['action']
        params = action['parameters']
        location_position = params['location_position']['value']
        location_city = params['location_city']['value']

        hospital_location = location_hospital(location_position, location_city)
        print(hospital_location)
        return create_message_location(f"먼저 {hospital_location[0]}의 위치로는 {hospital_location[1]}이며, 전화번호는 {hospital_location[2]}입니다. {hospital_location[3]}의 위치, {hospital_location[4]} 이고, 전화번호는 {hospital_location[5]}입니다.", location_position, location_city, hospital_location)
