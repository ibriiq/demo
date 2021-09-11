from django.http import response
from django.http.response import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
import requests
import json
from django.contrib.auth.decorators import login_required



# Billing view

def get_billing_info(request, data, headers, session):

    GetCustomers_url = 'http://192.168.2.19:96/api/values/GetCustomers'
    GetCustHistory_url = 'http://192.168.2.19:96/api/values/GetCustHistory'

    with session.post(GetCustomers_url, json=data, headers=headers) as response:
            GetCustomers = response.json()
    with session.post(GetCustHistory_url, json=data, headers=headers) as response:
            GetCustHistory = response.json()
    
    
    #     GetCustomers = requests.post(GetCustomers_url, json=data, headers=headers)
    #     GetCustomers = json.loads(GetCustomers.text)


    

    # GetCustHistory = requests.post(GetCustHistory_url, json=data, headers=headers)
    # GetCustHistory = json.loads(GetCustHistory.text)

    

    billing = {}

    
    billing["GetCustomers"] = GetCustomers
    billing["GetCustHistory"] = GetCustHistory

    return billing
