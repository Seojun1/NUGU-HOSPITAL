from flask import request, g, Blueprint
from flask_restx import Resource, Api
import requests
from utils import create_message_location, location_hospital

class locationAction(Resource):
    def post(self):
        data = request.get_json()
        action = data['action']
        params = action['parameters']

        province = params['location_position']['value']
        city = params['locaion_city']['value']
        hospital_name = params['hospital_name']['value']

        hospital_location = location_hospital(province, city, hospital_name)

        return create_message_location(f"{hospital_name}의 위치는 {hospital_location} 입니다.")
