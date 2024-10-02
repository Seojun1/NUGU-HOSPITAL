import requests
import re
import os
import requests
import pandas as pd
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os


def create_message(message, hospital_name, province, city):
    list_items = []
    for index, name in enumerate(hospital_name, start=1):
        list_items.append(
            {
                "token": f"{{{{{index * 111}}}}}",
                "header": {"text": str(index)},
                "body": {"text": name},
                "footer": {"text": f"{province} {city}"},
            }
        )

    return {
        "version": "2.0",
        "resultCode": "OK",
        "output": {"result": str(message)},
        "directives": [
            {
                "type": "Display.TextList2",
                "version": "1.0",
                "playServiceId": "{{playServiceId}}",
                "token": "{{token}}",
                "title": {"text": {"text": "조회된 병원 목록"}},
                "background": {
                    "image": {
                        "contentDescription": "{{STRING}}",
                        "sources": [
                            {"url": "http://someurl.com/name.png", "size": "LARGE"}
                        ],
                    }
                },
                "listItems": list_items,
            }
        ],
    }


def create_message_all(message, hospital_name, province, city):
    list_items = []
    for index, name in enumerate(hospital_name, start=1):
        list_items.append(
            {
                "token": f"{{{{{index * 111}}}}}",
                "header": {"text": str(index)},
                "body": {"text": name},
                "footer": {"text": f"{province} {city}"},
            }
        )

    return {
        "version": "2.0",
        "resultCode": "OK",
        "output": {"all_results": str(message)},
        "directives": [
            {
                "type": "Display.TextList2",
                "version": "1.0",
                "playServiceId": "{{playServiceId}}",
                "token": "{{token}}",
                "title": {"text": {"text": "조회된 병원 목록"}},
                "background": {
                    "image": {
                        "contentDescription": "{{STRING}}",
                        "sources": [
                            {"url": "http://someurl.com/name.png", "size": "LARGE"}
                        ],
                    }
                },
                "listItems": list_items,
            }
        ],
    }


def create_message_location(message, location_position, location_city, hospital_location):
    return {
        "version": "2.0",
        "resultCode": "OK",
        "output": {"location_results": str(message)},
        "directives": [
            {
  "type": "Display.TextList4",
  "version": "1.0",
  "playServiceId": "{{playServiceId}}",
  "token": "{{token}}",
  "title": {
    "logo": {
      "contentDescription": "{{contentDescription}}",
      "sources": [
        {
          "url": "blob:https://lordicon.com/7620b84f-be27-4b51-a3c8-f8f6a7ed0cd7"
        }
      ]
    },
    "text": {
      "text": f"{location_position} {location_city} 병원 위치 조회"
    }
  },
  "listItems": [
    {
      "token": "{{111}}",
      "header": {
        "text": hospital_location[2]
      },
      "body": [{
        "text": hospital_location[0]
      },
    {
        "text": f"전화번호 : {hospital_location[1]}"
    }], 
    },
    {
      "token": "{{222}}",
      "header": {
        "text": hospital_location[5]
      },
      "body": [{
        "text": hospital_location[3],
      },
      {
        "text": f"전화번호 : {hospital_location[4]}"

      }],
    },
  ]
}
        ],
    }


def create_holiday_message(message, hospital_name, province, city):
    list_items = []
    for index, name in enumerate(hospital_name, start=1):
        list_items.append(
            {
                "token": f"{{{{{index * 111}}}}}",
                "header": {"text": str(index)},
                "body": {"text": name},
                "footer": {"text": f"{province} {city}"},
            }
        )

    return {
        "version": "2.0",
        "resultCode": "OK",
        "output": {"holiday_result": str(message)},
        "directives": [
            {
                "type": "Display.TextList2",
                "version": "1.0",
                "playServiceId": "{{playServiceId}}",
                "token": "{{token}}",
                "title": {"text": {"text": "조회된 병원 목록"}},
                "background": {
                    "image": {
                        "contentDescription": "{{STRING}}",
                        "sources": [
                            {"url": "http://someurl.com/name.png", "size": "LARGE"}
                        ],
                    }
                },
                "listItems": list_items,
            }
        ],
    }


def create_holiday2_message(message, hospital_name, province, city):
    list_items = []
    for index, name in enumerate(hospital_name, start=1):
        list_items.append(
            {
                "token": f"{{{{{index * 111}}}}}",
                "header": {"text": str(index)},
                "body": {"text": name},
                "footer": {"text": f"{province} {city}"},
            }
        )

    return {
        "version": "2.0",
        "resultCode": "OK",
        "output": {"holiday_result2": str(message)},
        "directives": [
            {
                "type": "Display.TextList2",
                "version": "1.0",
                "playServiceId": "{{playServiceId}}",
                "token": "{{token}}",
                "title": {"text": {"text": "조회된 병원 목록"}},
                "background": {
                    "image": {
                        "contentDescription": "{{STRING}}",
                        "sources": [
                            {"url": "http://someurl.com/name.png", "size": "LARGE"}
                        ],
                    }
                },
                "listItems": list_items,
            }
        ],
    }


def create_weekend_message(
    message, saturday_hospitals, sunday_hospitals, province, city
):
    list_items = []

    for index, name in enumerate(saturday_hospitals, start=1):
        list_items.append(
            {
                "token": f"{{{{{index * 111}}}}}",
                "header": {"text": str(index)},
                "body": {"text": name},
                "footer": {"text": f"{province} {city} (토요일)"},
            }
        )

    for index, name in enumerate(sunday_hospitals, start=len(saturday_hospitals) + 1):
        list_items.append(
            {
                "token": f"{{{{{index * 111}}}}}",
                "header": {"text": str(index)},
                "body": {"text": name},
                "footer": {"text": f"{province} {city} (일요일)"},
            }
        )

    return {
        "version": "2.0",
        "resultCode": "OK",
        "output": {"weekend_result": str(message)},
        "directives": [
            {
                "type": "Display.TextList2",
                "version": "1.0",
                "playServiceId": "{{playServiceId}}",
                "token": "{{token}}",
                "title": {"text": {"text": "조회된 주말 운영 병원 목록"}},
                "background": {
                    "image": {
                        "contentDescription": "{{STRING}}",
                        "sources": [
                            {"url": "http://someurl.com/name.png", "size": "LARGE"}
                        ],
                    }
                },
                "listItems": list_items,
            }
        ],
    }


def create_weekend_all_message(
    message, saturday_hospitals, sunday_hospitals, province, city
):
    list_items = []

    for index, name in enumerate(saturday_hospitals, start=1):
        list_items.append(
            {
                "token": f"{{{{{index * 111}}}}}",
                "header": {"text": str(index)},
                "body": {"text": name},
                "footer": {"text": f"{province} {city} (토요일)"},
            }
        )

    for index, name in enumerate(sunday_hospitals, start=len(saturday_hospitals) + 1):
        list_items.append(
            {
                "token": f"{{{{{index * 111}}}}}",
                "header": {"text": str(index)},
                "body": {"text": name},
                "footer": {"text": f"{province} {city} (일요일)"},
            }
        )
    return {
        "version": "2.0",
        "resultCode": "OK",
        "output": {"weekend_all": str(message)},
        "directives": [
            {
                "type": "Display.TextList2",
                "version": "1.0",
                "playServiceId": "{{playServiceId}}",
                "token": "{{token}}",
                "title": {"text": {"text": "조회된 병원 목록"}},
                "background": {
                    "image": {
                        "contentDescription": "{{STRING}}",
                        "sources": [
                            {"url": "http://someurl.com/name.png", "size": "LARGE"}
                        ],
                    }
                },
                "listItems": list_items,
            }
        ],
    }


# 환경변수 Settings
BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))
decoding = os.environ.get('API_KEY')
url = os.environ.get('URL')

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


def location_hospital(location_position, location_city):
    params = {
        "serviceKey": decoding,
        "Q0": location_position,
        "Q1": location_city,
        "QZ": "",
        "QD": "D001",
        "QT": "",
        "QN": "",
        "ORD": "NAME",
        "pageNo": "1",
        "numOfRows": "2",
    }
    response = requests.get(url, params=params)

    # Parse the XML data
    root = ET.fromstring(response.text)

    duty_name_list = []

    # Example: Extracting all items from the XML
    for item in root.findall(".//item"):
        duty_add = item.find("dutyAddr").text
        duty_tel = item.find("dutyTel1").text
        duty_name = item.find("dutyName").text
        duty_name_list.append(duty_add)
        duty_name_list.append(duty_tel)
        duty_name_list.append(duty_name)

    return duty_name_list
