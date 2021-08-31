from django.http import response
from django.http.response import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
import requests
import json

# Create your views here.


def all_in_one(request):
    # requests.get("")
    if request.method == "GET":
        return render(request, "all_in_one/all_in_one.html")
    else:
        GetCustomers_url = 'http://192.168.2.19:97/api/values/GetCustomers'
        GetCustHistory_url = 'http://192.168.2.19:97/api/values/GetCustHistory'
        getCaawiyeInformation_url = 'http://192.168.2.19:97/api/values/getXallyeinfo'

        AccBalance_url = 'http://192.168.2.19:97/api/values/AccBalance'
        GetiCBSsubscriberInfo_url = 'http://192.168.2.19:97/api/values/GetiCBSsubscriberInfo'

        

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

        GetCustomers = requests.post(GetCustomers_url, json=data)
        GetCustomers = json.loads(GetCustomers.text)

        GetCustHistory = requests.post(GetCustHistory_url, json=data)
        GetCustHistory = json.loads(GetCustHistory.text)

        getCaawiyeInformation = requests.post(getCaawiyeInformation_url, json=data)
        getCaawiyeInformation = json.loads(getCaawiyeInformation.text)

        AccBalance = requests.post(AccBalance_url, json=data)
        AccBalance = json.loads(AccBalance.text)


        GetiCBSsubscriberInfo = requests.post(GetiCBSsubscriberInfo_url, json=data)
        GetiCBSsubscriberInfo = json.loads(GetiCBSsubscriberInfo.text)

        print("json response", GetiCBSsubscriberInfo)

        context = {"GetCustomers": GetCustomers, "GetCustHistory": GetCustHistory,
                "getCaawiyeInformation": getCaawiyeInformation, "GetiCBSsubscriberInfo" : GetiCBSsubscriberInfo ,"AccBalance" : AccBalance}

    
        return render(request, "all_in_one/all_in_one.html", context)



def get_billing(request):
    return ""


def get_sahal(request):
    return ""


def UpdateXallyeBlacklist(request):
    if request.is_ajax():
        response = {}
        UpdateXallyeBlacklist_url = 'http://192.168.2.19:97/api/values/UpdateXallyeBlacklist'
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
                "IsblackListed": request.POST["xaliye_status"],
                "txtDescription": request.POST["description"],
                "userid": "AABH"
            }
        }

        UpdateXallyeBlacklist = requests.post(
            UpdateXallyeBlacklist_url, json=data)
        UpdateXallyeBlacklist = json.loads(UpdateXallyeBlacklist.text)

        if UpdateXallyeBlacklist["responseBody"] == "Success":
            response["success"] = True
            response["msg"] = "Xaliye status of callsub " + \
                request.POST['callsub']+" is updated"
        else:
            response["success"] = False
            response["msg"] = "Something went wrong while updating xaliye information!!!"

        return JsonResponse(response)

    else:
        # return HttpResponseBadRequest()
        return render(request, "layout/handle_errors/handle_400.html", status=400)
