from django.http import response
from django.http.response import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
import requests
import json
from django.contrib.auth.decorators import login_required
from requests.api import request
from .views import xaliye, billing, IN, sahal, internet, options
from .views.billing import get_billing_info
from .views.IN import get_in_info
from .views.sahal import get_sahal_info
from .helpers import helper
from concurrent.futures import ThreadPoolExecutor
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




        with ThreadPoolExecutor(max_workers=50) as executor:
            with requests.Session() as session:
                billing_executer = executor.map(get_billing_info , [request]  , [data] , [headers]  , [session] , timeout=60)
                # billing_executer = executor.submit(get_billing_info , request  , data , headers  , session)
                IN_executer = executor.submit(get_in_info, request, data, headers, session)
                IN_executer = executor.submit(get_in_info, request, data, headers, session)
                sahal_executer = executor.submit(get_sahal_info, request, data, headers, session)
                xaliye_executer = executor.submit(xaliye.get_xaliye_info, request, data, headers, session)
                internet_executer = executor.submit(internet.get_internet_info, request, data, headers ,session)
                executor.shutdown(wait=True)
        

        for value in billing_executer:
            GetCustomers = value["GetCustomers"]
            GetCustHistory = value["GetCustHistory"]


        # billing here starts here
        # GetCustomers = billing_executer.result()["GetCustomers"]
        # GetCustHistory = billing_executer.result()["GetCustHistory"]
        # billing here ends here

       

        # get IN info start here
        AccBalance = IN_executer.result()["AccBalance"]
        GetiCBSsubscriberInfo = IN_executer.result()["GetiCBSsubscriberInfo"]
        # get IN info ends here

        # get sahal info starts here

        GetSahalinfo = sahal_executer.result()["GetSahalinfo"]
        GetSAHALinfoAcc = sahal_executer.result()["GetSAHALinfoAcc"]

        # get sahal info ends here


        # xaliye info beings here
        getCaawiyeInformation = xaliye_executer.result()
        # xaliye info ends here

        # get internet information start here

        DisplayINTERNETINFO = internet_executer.result()

        # get internet information ends here

        context = {
            'callsub': int(request.POST["callsub"]),
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
