from flask import Flask
from flask_restx import Api, Namespace
import os

from .health import HealthCheck
from .all_hospital import AllHospitalAction, AllHospitalAction2
from .holiday_hospital import HolidayHospitalAction, HolidayHospitalAction2
from .weekend_hospital import WeekendHospitalAction, WeekendAllHospitalAction
from .locaion_hospital_action import locationAction

class NuguApi(Flask):
    def __init__(self):
        super().__init__(__name__)
        self.api = Api(self, title="NUGU Backend Proxy", version="0.1")
        ns = Namespace("")
        self.api.add_resource(HealthCheck, "/health")

        self.api.add_resource(AllHospitalAction, "/my_hostpital_action")
        self.api.add_resource(AllHospitalAction2, "/all_myhospital_action")

        self.api.add_resource(HolidayHospitalAction, "/holiday_hospital_action")
        self.api.add_resource(HolidayHospitalAction2, "/holiday_hospital_action2")

        self.api.add_resource(WeekendHospitalAction, "/weekend_hospital_action")
        self.api.add_resource(WeekendAllHospitalAction, "/weekend_hostpital_all")

        self.api.add_resource(locationAction, "/location_hospital_action")



