from django.http import response
from django.http.response import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
import requests
import json
from django.contrib.auth.decorators import login_required

# sahal view .


def get_sahal_info(request, data, headers):
    # get sahal info for main account start here

    GetSahalinfo_url = 'http://192.168.2.19:96/api/values/GetSahalinfo'
    GetSahalinfo = requests.post(GetSahalinfo_url, json=data, headers=headers)
    GetSahalinfo = json.loads(GetSahalinfo.text)

    # if "Message" not in GetSahalinfo:
    #     GetSahalinfo = GetSahalinfo["serviceInfo"]["responseAttributes"]["SubscriberInfo"]

    # get sahal info for main account ends here

    # get sahal info for partner start here

    GetSAHALinfoAcc_url = 'http://192.168.2.19:96/api/values/GetSAHALinfoAcc'
    GetSAHALinfoAcc = requests.post(GetSAHALinfoAcc_url, json=data, headers=headers)
    GetSAHALinfoAcc = json.loads(GetSAHALinfoAcc.text)

    if "Message" not in GetSAHALinfoAcc:
        GetSAHALinfoAcc = GetSAHALinfoAcc["serviceInfo"]["responseAttributes"]["PartnerInfo"]

    # get sahal info for partner start here

    sahal = {}

    sahal["GetSahalinfo"] = GetSahalinfo
    sahal["GetSAHALinfoAcc"] = GetSAHALinfoAcc

    return sahal
