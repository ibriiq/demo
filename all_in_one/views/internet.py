from django.http import response
from django.http.response import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
import requests
import json
from django.contrib.auth.decorators import login_required

# sahal view .


def get_internet_info(request, data, headers, session):
    DisplayINTERNETINFO_url = 'http://192.168.2.19:96/api/values/DisplayINTERNETINFO'

    with session.post(DisplayINTERNETINFO_url, json=data, headers=headers) as response:
            DisplayINTERNETINFO = response.json()


    # if not "Message" in DisplayINTERNETINFO:
    #     DisplayINTERNETINFO = DisplayINTERNETINFO['responseBody']

    internet = {}
    return DisplayINTERNETINFO