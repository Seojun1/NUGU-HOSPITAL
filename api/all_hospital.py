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
        if len(hospital_name) == 0:
            return create_message(f"현재 조회되는 병원이 없습니다. 다음에 저를 다시 불러주세요!")
        else:
            return create_message(f"현재 조회되는 병원으로는 총 3곳으로, {hospital_name} 등등이 있습니다. 추가적으로, 더 많은 병원을 목소리로 듣고 싶으시다면 '네'라고 말씀해주세요.", hospital_name, province, city)

class AllHospitalAction2(Resource):
    def post(self):
        data = request.get_json()
        action = data['action']
        params = action['parameters']

        province = params['location']['value']
        city = params['city']['value']

        print("백엔드 값 요청 : ", province, city)
        hospital_name = all_hospital_action2(province, city)
        return create_message_all(f"총 {len(hospital_name)}곳으로, {hospital_name}이 있습니다.", hospital_name, province, city)
