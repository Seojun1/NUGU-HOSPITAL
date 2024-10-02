from flask import request, g, Blueprint
from flask_restx import Resource, Api, Namespace

class HealthCheck(Resource):
    def get(self):
        return "Good"