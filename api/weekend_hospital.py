from flask import request, g, Blueprint
from flask_restx import Resource, Api
import requests
from utils import create_weekend_message, weekend_hospital, weekend_all_hospital, create_weekend_all_message

class WeekendHospitalAction(Resource):
    def post(self):
        data = request.get_json()
        action = data['action']
        params = action['parameters']

        province = params['weekend_location']['value']
        city = params['weekend_city']['value']

        saturday_hospitals, sunday_hospitals = weekend_hospital(province, city)
        hospitals_cnt = len(saturday_hospitals) + len(sunday_hospitals)

        all_list = saturday_hospitals + sunday_hospitals

        if hospitals_cnt == 0:
            return create_weekend_message(f"주말에도 운영하는 병원은 0곳으로, 있지 않은 것 같습니다.")
        else:
            return create_weekend_message(f"주말에도 운영하는 병원은 {hospitals_cnt}곳으로, 토요일은 {saturday_hospitals}, 일요일은 {sunday_hospitals} 등등이 있습니다.", saturday_hospitals, sunday_hospitals, province, city)

class WeekendAllHospitalAction(Resource):
    def post(self):
        data = request.get_json()
        action = data['action']
        params = action['parameters']
        province = params['weekend_location']['value']
        city = params['weekend_city']['value']

        saturday_hospitals, sunday_hospitals = weekend_all_hospital(province, city)

        return create_weekend_all_message(f"토요일은 {saturday_hospitals}이 있고, 일요일은 {sunday_hospitals}이 있습니다.", saturday_hospitals, sunday_hospitals, province, city)
