from django.http import response
from django.http.response import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
import requests
import json
from django.contrib.auth.decorators import login_required

# sahal view .


def get_internet_info(request, data, headers):
    DisplayINTERNETINFO_url = 'http://192.168.2.19:96/api/values/DisplayINTERNETINFO'

    DisplayINTERNETINFO = requests.post(
        DisplayINTERNETINFO_url, json=data, headers=headers)
    DisplayINTERNETINFO = json.loads(DisplayINTERNETINFO.text)

    # if not "Message" in DisplayINTERNETINFO:
    #     DisplayINTERNETINFO = DisplayINTERNETINFO['responseBody']

    internet = {}
    return DisplayINTERNETINFO