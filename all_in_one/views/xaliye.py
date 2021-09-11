from django.http import response
from django.http.response import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
import requests
import json
from django.contrib.auth.decorators import login_required

# Xaliye view .


def get_xaliye_info(request, data, headers, session):
    getXaliyeInformation_url = 'http://192.168.2.19:96/api/values/getXallyeinfo'
    with session.post(getXaliyeInformation_url, json=data, headers=headers) as response:
            getXaliyeInformation = response.json()
    return getXaliyeInformation


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


def UpdateXallyeDisable(request):
    if request.is_ajax():
        response = {}
        UpdateXallyeDisable_url = 'http://192.168.2.19:97/api/values/UpdateXallyeDisable'
        data = {
            "requestId": "01bd2631-1a82-42b5-8e9d-5ae0c51d72cb",
            "schemaVersion": "1.0",
            "requestHeader": {
                "timestamp": "20201126101346",
                "apikey": "APICCAre",
                "apiPassword": "0013801971c69437e3130b7cffd2c04cb17ca659"
            },
            "requestBody": {
                "callsub": request.POST["callsub"],
                "IsEnabled": request.POST["xaliye_status"],
                "txtDescription": request.POST["description"],
                "userid": "AABH"
            }
        }

        UpdateXallyeDisable = requests.post(
            UpdateXallyeDisable_url, json=data)
        UpdateXallyeDisable = json.loads(UpdateXallyeDisable.text)

        print(UpdateXallyeDisable)

        if UpdateXallyeDisable["responseBody"] == "Success":
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


# update xaliye reset bin
@login_required
def UpdateXallyeresetbin(request):
    if request.is_ajax():
        response = {}
        UpdateXallyeresetbin_url = 'http://192.168.2.19:97/api/values/UpdateXallyeeResetPin'
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
                "Pin": request.POST["resetbin"],
                "txtDescription": request.POST["description"],
                "userid": "AABH"
            }
        }

        UpdateXallyeresetbin = requests.post(
            UpdateXallyeresetbin_url, json=data)
        UpdateXallyeresetbin = json.loads(UpdateXallyeresetbin.text)

        print(UpdateXallyeresetbin)

        if UpdateXallyeresetbin["responseBody"] == "Success":
            response["success"] = True
            response["msg"] = "The bin of " + \
                request.POST['callsub']+" is reseted successfully"
        else:
            response["success"] = False
            response["msg"] = "Something went wrong while Reseting xaliye bin !!!"

        return JsonResponse(response)
    else:
        # return HttpResponseBadRequest()
        return render(request, "layout/handle_errors/handle_400.html", status=400)
