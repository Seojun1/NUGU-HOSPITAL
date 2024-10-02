from flask import request, g, Blueprint
from flask_restx import Resource, Api
import requests
from utils import create_message, all_hospital, create_message_all, all_hospital_action2

class AllHospitalAction(Resource):
    def post(self):
        data = request.get_json()
        action = data['action']
        params = action['parameters']

        province = params['location']['value']
        city = params['city']['value']

        print("백엔드 값 요청 : ", province, city)
        hospital_name = all_hospital(province, city)
        return create_message(f"{hospital_name} 등등이 있습니다. 더 많은 병원을 알고싶으시다면 '네'라고 말씀해주세요.")

class AllHospitalAction2(Resource):
    def post(self):
        data = request.get_json()
        action = data['action']
        params = action['parameters']

        province = params['location']['value']
        city = params['city']['value']

        print("백엔드 값 요청 : ", province, city)
        hospital_name = all_hospital_action2(province, city)
        return create_message_all(f"총 {len(hospital_name)}곳으로, {hospital_name}이 있습니다.")
