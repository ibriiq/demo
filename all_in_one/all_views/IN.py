from django.http import response
from django.http.response import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
import requests
import json
from django.contrib.auth.decorators import login_required
from datetime import datetime


def get_in_info(request, data, headers):
    AccBalance_url = 'http://192.168.2.19:96/api/values/AccBalance'
    GetiCBSsubscriberInfo_url = 'http://192.168.2.19:96/api/values/GetiCBSsubscriberInfo'

    AccBalance = requests.post(AccBalance_url, json=data, headers=headers)
    AccBalance = json.loads(AccBalance.text)

    GetiCBSsubscriberInfo = requests.post(
        GetiCBSsubscriberInfo_url, json=data, headers=headers)
    GetiCBSsubscriberInfo = json.loads(GetiCBSsubscriberInfo.text)

    IN = {}

    if not "Message" in AccBalance:
        AccBalance = AccBalance["responseBody"]

    # if not "Message" in GetiCBSsubscriberInfo:
        # GetiCBSsubscriberInfo = GetiCBSsubscriberInfo["responseBody"]

    if not "Message" in AccBalance and len(AccBalance) > 0:
        for i in range(len(AccBalance)):
            if AccBalance[i].get("accountTypeField") == "4201":
                AccBalance[i].update(
                    {
                        'accountTypeField': "Data Bundle",
                        'amountField': str((int(AccBalance[i].get("amountField")) / 1024)/1024) + " MB"

                    }
                )

            if AccBalance[i].get("accountTypeField") == "5003":
                AccBalance[i].update(
                    {
                        'accountTypeField': "Local sms",
                        # 'amountField': str((int(AccBalance[i].get("amountField")) / 1024)/1024) + " MB"

                    }
                )

            if AccBalance[i].get("accountTypeField") == "2000":
                AccBalance[i].update(
                    {
                        'accountTypeField': "Main Account",
                        # 'amountField': str((int(AccBalance[i].get("amountField")) / 1024)/1024) + " MB"

                    }
                )

            if AccBalance[i].get("accountTypeField") == "2505":
                AccBalance[i].update(
                    {
                        'accountTypeField': "Emt account",
                        # 'amountField': str((int(AccBalance[i].get("amountField")) / 1024)/1024) + " MB"

                    }
                )

            if AccBalance[i].get("accountTypeField") == "5005":
                AccBalance[i].update(
                    {
                        'accountTypeField': "Staff hadal",
                        'amountField': str((int(AccBalance[i].get("amountField")) / 60)) + " Minutes"

                    }
                )

            AccBalance[i].update(
                {
                    'applyTimeField':  datetime.strptime(AccBalance[i].get("applyTimeField"), '%Y%m%d').strftime('%m/%d/%Y'),
                    'expireTimeField':  datetime.strptime(AccBalance[i].get("expireTimeField"), '%Y%m%d').strftime('%m/%d/%Y'),
                })

    IN["AccBalance"] = AccBalance

    if not "Message" in GetiCBSsubscriberInfo and len(GetiCBSsubscriberInfo["responseBody"]) > 0:

        # GetiCBSsubscriberInfo = GetiCBSsubscriberInfo[0]
        print(GetiCBSsubscriberInfo)
        GetiCBSsubscriberInfo["responseBody"][0].update(
            {
                'lastActivationDateField': datetime.strptime(GetiCBSsubscriberInfo["responseBody"][0].get("lastActivationDateField"), '%Y%m%d').strftime('%m/%d/%Y'),
                'suspendStopField': datetime.strptime(GetiCBSsubscriberInfo["responseBody"][0].get("suspendStopField"), '%Y%m%d').strftime('%m/%d/%Y'),
                'activationDateField': datetime.strptime(GetiCBSsubscriberInfo["responseBody"][0].get("activationDateField"), '%Y%m%d%H%M%S').strftime('%m/%d/%Y %H:%M:%S')
            })

    IN["GetiCBSsubscriberInfo"] = GetiCBSsubscriberInfo

    return IN


def iCBSWebdisClaimMissing(request):
    if request.is_ajax():
        response = {}
        headers = {
            "Authorization": request.session.get("token_type") + " " + request.session.get("access_token")
        }
        data = {
            "requestId": "01bd2631-1a82-42b5-8e9d-5ae0c51d72cb",
            "schemaVersion": "1.0",
            "requestHeader": {
                "timestamp": "20201126101346",
                "apikey": "APICCare",
                "apiPassword": "0013801971c69437e3130b7cffd2c04cb17ca659"
            },
            "requestBody": {
                "callsub": "90"+request.POST["callsub"]
            }

        }
        iCBSWebdisClaimMissing_url = 'http://192.168.2.19:96/api/values/iCBSWebdisClaimMissing'
        iCBSWebdisClaimMissing = requests.post(
            iCBSWebdisClaimMissing_url, json=data, headers=headers)
        iCBSWebdisClaimMissing = json.loads(iCBSWebdisClaimMissing.text)
     
        if "Message" in iCBSWebdisClaimMissing:
            response["success"] = False
            response["msg"] = iCBSWebdisClaimMissing["Message"]
        else:
            response["success"] = True
            response["msg"] = iCBSWebdisClaimMissing["responseBody"]

        return JsonResponse(response)
    else:
        return render(request, "layout/handle_errors/handle_400.html", status=400)






def iCBSWebBlacklist(request):
    if request.is_ajax():
        response = {}
        headers = {
            "Authorization": request.session.get("token_type") + " " + request.session.get("access_token")
        }
        data = {
            "requestId": "01bd2631-1a82-42b5-8e9d-5ae0c51d72cb",
            "schemaVersion": "1.0",
            "requestHeader": {
                "timestamp": "20201126101346",
                "apikey": "APICCare",
                "apiPassword": "0013801971c69437e3130b7cffd2c04cb17ca659"
            },
            "requestBody": {
                "callsub": "90"+request.POST["callsub"]
            }

        }
        iCBSWebBlacklist_url = 'http://192.168.2.19:96/api/values/iCBSWebBlacklist'
        iCBSWebBlacklist = requests.post(
            iCBSWebBlacklist_url, json=data, headers=headers)
        iCBSWebBlacklist = json.loads(iCBSWebBlacklist.text)
     
        if "Message" in iCBSWebBlacklist:
            response["success"] = False
            response["msg"] = iCBSWebBlacklist["Message"]
        else:
            response["success"] = True
            response["msg"] = iCBSWebBlacklist["responseBody"]

        return JsonResponse(response)
    else:
        return render(request, "layout/handle_errors/handle_400.html", status=400)
