from django.http import response
from django.http.response import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
import requests
import json
from django.contrib.auth.decorators import login_required


#
def Getcenters(headers):
    data = {
        "requestId": "01bd2631-1a82-42b5-8e9d-5ae0c51d72cb",
        "schemaVersion": "1.0",
        "requestHeader": {
            "timestamp": "20201126101346",
            "apikey": "APICCare",
            "apiPassword": "0013801971c69437e3130b7cffd2c04cb17ca659"
        }
    }
    Getcenters_url = 'http://192.168.2.19:96/api/values/Getcenters'

    Getcenters = requests.post(
        Getcenters_url, json=data, headers=headers)
    Getcenters = json.loads(Getcenters.text)

    return Getcenters


#
def GetDepts(headers):
    data = {
        "requestId": "01bd2631-1a82-42b5-8e9d-5ae0c51d72cb",
        "schemaVersion": "1.0",
        "requestHeader": {
            "timestamp": "20201126101346",
            "apikey": "APICCare",
            "apiPassword": "0013801971c69437e3130b7cffd2c04cb17ca659"
        }
    }
    GetDepts_url = 'http://192.168.2.19:96/api/values/GetDepts'

    GetDepts = requests.post(
        GetDepts_url, json=data, headers=headers)
    GetDepts = json.loads(GetDepts.text)

    return GetDepts


#
def CCAREGroups(headers):
    data = {
        "requestId": "01bd2631-1a82-42b5-8e9d-5ae0c51d72cb",
        "schemaVersion": "1.0",
        "requestHeader": {
            "timestamp": "20201126101346",
            "apikey": "APICCare",
            "apiPassword": "0013801971c69437e3130b7cffd2c04cb17ca659"
        }
    }
    CCAREGroups_url = 'http://192.168.2.19:96/api/values/CCAREGroups'

    CCAREGroups = requests.post(
        CCAREGroups_url, json=data, headers=headers)
    CCAREGroups = json.loads(CCAREGroups.text)

    return CCAREGroups




#
def CompType(headers):
    data = {
        "requestId": "01bd2631-1a82-42b5-8e9d-5ae0c51d72cb",
        "schemaVersion": "1.0",
        "requestHeader": {
            "timestamp": "20201126101346",
            "apikey": "APICCare",
            "apiPassword": "0013801971c69437e3130b7cffd2c04cb17ca659"
        }
    }
    CompType_url = 'http://192.168.2.19:96/api/values/CompType'

    CompType = requests.post(
        CompType_url, json=data, headers=headers)
    CompType = json.loads(CompType.text)

    return CompType




#
def gsmfeatures(headers):
    data = {
        "requestId": "01bd2631-1a82-42b5-8e9d-5ae0c51d72cb",
        "schemaVersion": "1.0",
        "requestHeader": {
            "timestamp": "20201126101346",
            "apikey": "APICCare",
            "apiPassword": "0013801971c69437e3130b7cffd2c04cb17ca659"
        }
    }
    gsmfeatures_url = 'http://192.168.2.19:96/api/values/gsmfeatures'

    
    gsmfeatures = requests.post(
        gsmfeatures_url, json=data, headers=headers)
    gsmfeatures = json.loads(gsmfeatures.text)

    return gsmfeatures