from django.http import response
from django.http.response import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
import requests
import json
from django.contrib.auth.decorators import login_required
from requests.api import request
from .all_views import xaliye, billing, IN, sahal, internet, options
from .helpers import helper
# from

# Create your views here.


def all_in_one(request):
    headers = {
            "Authorization": request.session.get("token_type") + " " + request.session.get("access_token")
        }

    if request.method == "GET":
        context = {
            "Getcenters": helper.Getcenters(headers)["responseBody"],
            "CompType": helper.CompType(headers)["responseBody"],
            "GetDepts": helper.GetDepts(headers)["responseBody"],
            "CCAREGroups": helper.CCAREGroups(headers)["responseBody"],
            "gsmfeatures": helper.gsmfeatures(headers)["responseBody"]
            }

        return render(request, "all_in_one/all_in_one.html", context)
    else:

        
        data = {
            "requestId": "01bd2631-1a82-42b5-8e9d-5ae0c51d72cb",
            "schemaVersion": "1.0",
            "requestHeader": {
                "timestamp": "20201126101346",
                "apikey": "ShortCodes",
                "apiPassword": "0013801971c69437e3130b7cffd2c04cb17ca659"
            },
            "requestBody": {
                "callsub": request.POST["callsub"],
                "AllowToViewRestrictedBalGrps": True
            }
        }

        # billing here starts here
        GetCustomers = billing.get_billing_info(
            request, data, headers)["GetCustomers"]
        GetCustHistory = billing.get_billing_info(request, data, headers)[
            "GetCustHistory"]
        # billing here ends here

        # xaliye info beings here
        getCaawiyeInformation = xaliye.get_xaliye_info(request, data, headers)
        # xaliye info ends here

        # get IN info start here
        AccBalance = IN.get_in_info(request, data, headers)["AccBalance"]
        GetiCBSsubscriberInfo = IN.get_in_info(
            request, data, headers)["GetiCBSsubscriberInfo"]
        # get IN info ends here

        # get sahal info starts here

        GetSahalinfo = sahal.get_sahal_info(
            request, data, headers)["GetSahalinfo"]
        GetSAHALinfoAcc = sahal.get_sahal_info(
            request, data, headers)["GetSAHALinfoAcc"]

        # get sahal info ends here

        # get internet information start here

        DisplayINTERNETINFO = internet.get_internet_info(
            request, data, headers)

        # get internet information ends here

        context = {
            'callsub': request.POST["callsub"],
            "GetCustomers": GetCustomers, "GetCustHistory": GetCustHistory,
            "getCaawiyeInformation": getCaawiyeInformation, "GetiCBSsubscriberInfo": GetiCBSsubscriberInfo,
            "AccBalance": AccBalance, "GetSahalinfo": GetSahalinfo,
            "GetSAHALinfoAcc": GetSAHALinfoAcc, "DisplayINTERNETINFO": DisplayINTERNETINFO,
            

            # helpers start here
            "Getcenters": helper.Getcenters(headers)["responseBody"],
            "CompType": helper.CompType(headers)["responseBody"],
            "GetDepts": helper.GetDepts(headers)["responseBody"],
            "CCAREGroups": helper.CCAREGroups(headers)["responseBody"],
            "gsmfeatures": helper.gsmfeatures(headers)["responseBody"]
            # helpers ends here

            
        }

        return render(request, "all_in_one/all_in_one.html", context)
