from flask import request, g, Blueprint
from flask_restx import Resource, Api
import requests
from utils import create_holiday_message, holiday_hospital, create_holiday2_message, holiday_hospital2

class HolidayHospitalAction(Resource):
    def post(self):
        data = request.get_json()
        action = data['action']
        params = action['parameters']

        province = params['holiday_location']['value']
        city = params['holiday_city']['value']

        hospital_name = holiday_hospital(province, city)
        if len(hospital_name) == 0:
            return create_holiday_message(f"공휴일에도 운영하는 병원은 0곳으로, 있지 않은 것 같습니다. 다른 도움이 필요하면 저를 다시 호출해주세요.")
        else:
            return create_holiday_message(f"공휴일에도 운영하는 병원 3곳을 먼저 알려드릴게요. 공휴일에 운영하는 병원은 {hospital_name} 이 있습니다. 이 외에도 '네'라고 말씀하시면 공휴일에 운영하는 병원 15곳을 더 알려드릴게요.", hospital_name, province, city)

class HolidayHospitalAction2(Resource):
    def post(self):
        data = request.get_json()
        action = data['action']
        params = action['parameters']

        province = params['holiday_location']['value']
        city = params['holiday_city']['value']

        hospital_name = holiday_hospital2(province, city)

        return create_holiday2_message(f"{hospital_name} 이 있습니다.", hospital_name, province, city)
