import requests
import re
import os
import requests
import pandas as pd
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os

def create_message(message):
    return {"version": "2.0", "resultCode": "OK", "output": {"result": str(message)}}


def create_message_all(message):
    return {
        "version": "2.0",
        "resultCode": "OK",
        "output": {"all_results": str(message)},
    }


def create_message_location(message):
    return {
        "version": "2.0",
        "resultCode": "OK",
        "output": {"location_result": str(message)},
    }


def create_holiday_message(message):
    return {
        "version": "2.0",
        "resultCode": "OK",
        "output": {"holiday_result": str(message)},
    }


def create_holiday2_message(message):
    return {
        "version": "2.0",
        "resultCode": "OK",
        "output": {"holiday_result2": str(message)},
    }


def create_weekend_message(message):
    return {
        "version": "2.0",
        "resultCode": "OK",
        "output": {"weekend_result": str(message)},
    }


def create_weekend_all_message(message):
    return {
        "version": "2.0",
        "resultCode": "OK",
        "output": {"weekend_all": str(message)},
    }


# 환경변수 Settings
load_dotenv()
decoding = os.environ.get('API_KEY')
url = os.environ.get("URL")

def all_hospital(province, city):
    params = {
        "serviceKey": decoding,
        "Q0": province,
        "Q1": city,
        "QZ": "",
        "QD": "D001",
        "QT": "1",
        "QN": "",
        "ORD": "NAME",
        "pageNo": "1",
        "numOfRows": "3",
    }
    response = requests.get(url, params=params)

    # Parse the XML data
    root = ET.fromstring(response.text)

    duty_name_list = []

    # Example: Extracting all items from the XML
    for item in root.findall(".//item"):
        duty_name = item.find("dutyName").text
        duty_name_list.append(duty_name)

    return duty_name_list


def all_hospital_action2(province, city):
    params = {
        "serviceKey": decoding,
        "Q0": province,
        "Q1": city,
        "QZ": "",
        "QD": "D001",
        "QT": "1",
        "QN": "",
        "ORD": "NAME",
        "pageNo": "1",
        "numOfRows": "15",
    }
    response = requests.get(url, params=params)

    # Parse the XML data
    root = ET.fromstring(response.text)

    duty_name_list = []

    # Example: Extracting all items from the XML
    for item in root.findall(".//item"):
        duty_name = item.find("dutyName").text
        duty_name_list.append(duty_name)

    return duty_name_list


def holiday_hospital(province, city):
    params = {
        "serviceKey": decoding,
        "Q0": province,
        "Q1": city,
        "QZ": "",
        "QD": "D001",
        "QT": "8",
        "QN": "",
        "ORD": "NAME",
        "pageNo": "1",
        "numOfRows": "3",
    }
    response = requests.get(url, params=params)

    # Parse the XML data
    root = ET.fromstring(response.text)

    duty_name_list = []

    # Example: Extracting all items from the XML
    for item in root.findall(".//item"):
        duty_name = item.find("dutyName").text
        duty_name_list.append(duty_name)

    return duty_name_list


def holiday_hospital2(province, city):
    params = {
        "serviceKey": decoding,
        "Q0": province,
        "Q1": city,
        "QZ": "",
        "QD": "D001",
        "QT": "8",
        "QN": "",
        "ORD": "NAME",
        "pageNo": "1",
        "numOfRows": "15",
    }
    response = requests.get(url, params=params)

    # Parse the XML data
    root = ET.fromstring(response.text)

    duty_name_list = []

    # Example: Extracting all items from the XML
    for item in root.findall(".//item"):
        duty_name = item.find("dutyName").text
        duty_name_list.append(duty_name)

    return duty_name_list


def weekend_hospital(province, city):
    saturday_clinics = []
    sunday_clinics = []

    for qt in ["6", "7"]:  # 6: 토요일, 7: 일요일
        params = {
            "serviceKey": decoding,
            "Q0": province,
            "Q1": city,
            "QZ": "",
            "QD": "D001",
            "QT": qt,
            "QN": "",
            "ORD": "NAME",
            "pageNo": "1",
            "numOfRows": "",
        }
        response = requests.get(url, params=params)
        root = ET.fromstring(response.text)

        for item in root.findall(".//item"):
            duty_name = item.find("dutyName").text
            if qt == "6":
                saturday_clinics.append(duty_name)
            else:
                sunday_clinics.append(duty_name)

    return saturday_clinics, sunday_clinics


def weekend_all_hospital(province, city):
    saturday_clinics = []
    sunday_clinics = []

    for qt in ["6", "7"]:  # 6: 토요일, 7: 일요일
        params = {
            "serviceKey": decoding,
            "Q0": province,
            "Q1": city,
            "QZ": "",
            "QD": "D001",
            "QT": qt,
            "QN": "",
            "ORD": "NAME",
            "pageNo": "1",
            "numOfRows": "10",
        }
        response = requests.get(url, params=params)
        root = ET.fromstring(response.text)

        for item in root.findall(".//item"):
            duty_name = item.find("dutyName").text
            if qt == "6":
                saturday_clinics.append(duty_name)
            else:
                sunday_clinics.append(duty_name)

    return saturday_clinics, sunday_clinics


def location_hospital(province, city, hospital_name):
    params = {
        "serviceKey": decoding,
        "Q0": province,
        "Q1": city,
        "QZ": "",
        "QD": "D001",
        "QT": "",
        "QN": hospital_name,
        "ORD": "NAME",
        "pageNo": "1",
        "numOfRows": "1",
    }
    response = requests.get(url, params=params)

    # Parse the XML data
    root = ET.fromstring(response.text)

    duty_name_list = []

    # Example: Extracting all items from the XML
    for item in root.findall(".//item"):
        duty_name = item.find("dutyAddr").text
        duty_name_list.append(duty_name)

    return duty_name_list
