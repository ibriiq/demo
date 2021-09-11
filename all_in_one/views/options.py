from django.http import response
from django.http.response import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
import requests
import json
from django.contrib.auth.decorators import login_required

# sahal view .


def DisplayPhoneDirectory(request):
    if request.is_ajax():
        response = {}
        DisplayPhoneDirectory_url = 'http://192.168.2.19:96/api/values/DisplayPhoneDirectory'
        headers = {
            "Authorization": request.session.get("token_type") + " " + request.session.get("access_token")
        }

        data = {
            "requestId": "01bd2631-1a82-42b5-8e9d-5ae0c51d72cb",
            "schemaVersion": "1.0",
            "requestHeader": {
                "timestamp": "20201126101346",
                "apikey": "APICCAre",
                "apiPassword": "0013801971c69437e3130b7cffd2c04cb17ca659"
            },
            "requestBody": {
                "Searchby":  request.POST["search_by"],
                "SearchValue": request.POST["search_value"],
                "UserID": "golbs1337"
            }
        }

        DisplayPhoneDirectory = requests.post(
            DisplayPhoneDirectory_url, json=data, headers=headers)
        status_code = DisplayPhoneDirectory.status_code
        DisplayPhoneDirectory = json.loads(DisplayPhoneDirectory.text)

        # print(DisplayPhoneDirectory["responseHeader"]["resultMessage"])

        print(DisplayPhoneDirectory)

        if "Message" in DisplayPhoneDirectory:
            response["success"] = False
            response["status"] = status_code
            response["msg"] = DisplayPhoneDirectory["Message"]

        elif DisplayPhoneDirectory["responseHeader"]["resultMessage"] == "SUCCESS":
            response["success"] = True
            response["msg"] = "Xaliye status of callsub " + \
                request.POST['search_value']+" is updated"
            response["data"] = DisplayPhoneDirectory["responseBody"]
        else:
            response["success"] = False
            response["status"] = status_code
            response["msg"] = "Something went wrong while updating xaliye information!!!"

        return JsonResponse(response)

    else:
        # return HttpResponseBadRequest()
        return render(request, "layout/handle_errors/handle_400.html", status=400)


def DisplayArea(request):
    if request.is_ajax():
        response = {}
        DisplayArea_url = 'http://192.168.2.19:97/api/values/DisplayArea'
        data = {
            "requestId": "01bd2631-1a82-42b5-8e9d-5ae0c51d72cb",
            "schemaVersion": "1.0",
            "requestHeader": {
                "timestamp": "20201126101346",
                "apikey": "APICCAre",
                "apiPassword": "0013801971c69437e3130b7cffd2c04cb17ca659"
            },
            "requestBody": {
                "Searchby":  request.POST["search_by"],
                "SearchValue": request.POST["search_value"],
                "UserID": "golbs1337"
            }
        }

        DisplayArea = requests.post(
            DisplayArea_url, json=data)
        DisplayArea = json.loads(DisplayArea.text)

        # print(DisplayArea["responseHeader"]["resultMessage"])

        if DisplayArea["responseHeader"]["resultMessage"] == "SUCCESS":
            response["success"] = True
            response["msg"] = "Xaliye status of callsub " + \
                request.POST['search_value']+" is updated"
            response["data"] = DisplayArea["responseBody"]
        else:
            response["success"] = False
            response["msg"] = "Something went wrong while updating xaliye information!!!"

        return JsonResponse(response)

    else:
        # return HttpResponseBadRequest()
        return render(request, "layout/handle_errors/handle_400.html", status=400)








def SaveSahalComp(request):
    if request.is_ajax():


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
                "Custname": request.POST["Custname"],
                "comptype": request.POST["comptype"],
                "Center": request.POST["Center"] ,
                "reciever": request.POST["reciever"],
                "amount": request.POST["amount"],
                "Userid": request.session["loggin_user"]["userid"]
                }
            }

        print("the data of sahal complaints = ", data)



        headers = {
            "Authorization": request.session.get("token_type") + " " + request.session.get("access_token")
        }
    
        response = {}
        SaveSahalComp_url = 'http://192.168.2.19:96/api/values/SaveSahalComp'
        SaveSahalComp = requests.post(  SaveSahalComp_url, json=data, headers = headers)
        SaveSahalComp = json.loads(SaveSahalComp.text)

        print("the complaint = ",SaveSahalComp)

        if SaveSahalComp["responseHeader"]["resultMessage"] == "SUCCESS":
            response["success"] = True
            response["msg"] = SaveSahalComp["responseBody"]
        else:
            response["success"] = False
            response["msg"] = "Something went wrong while updating xaliye information!!!"

        return JsonResponse(response)
        
        

    else:
        # return HttpResponseBadRequest()
        return render(request, "layout/handle_errors/handle_400.html", status=400)
    


    # return SaveSahalComp




def SaveNewUsers(request):
    if request.is_ajax():


        data = {
                    "requestId": "01bd2631-1a82-42b5-8e9d-5ae0c51d72cb",
                    "schemaVersion": "1.0",
                    "requestHeader": {
                    "timestamp": "20201126101346",
                    "apikey": "APICCAre",
                        "apiPassword": "0013801971c69437e3130b7cffd2c04cb17ca659"
                    },
                    "requestBody": {
                    "callsub":  request.POST["callsub"],
                    "Name": request.POST["name"],
                    "Groups": request.POST["Group"],
                    "dept": request.POST["dept"],
                    "UserID": request.POST["UserID"],
                    "UserName": request.POST["UserName"],
                    "Status": request.POST["status"],
                    "Center": request.POST["Center"],
                    "ViewBalGroup": "1",
                    "CerUserID": request.session.get("loggin_user")["userid"]
                    }
                }

        print("the data of SaveNewUsers = ", data)



        headers = {
            "Authorization": request.session.get("token_type") + " " + request.session.get("access_token")
        }
    
        response = {}
        SaveNewUsers_url = 'http://192.168.2.19:96/api/values/SaveNewUsers'
        SaveNewUsers = requests.post(  SaveNewUsers_url, json=data, headers = headers)
        SaveNewUsers = json.loads(SaveNewUsers.text)

        print("the SaveNewUsers = ",SaveNewUsers)

        if SaveNewUsers["responseHeader"]["resultMessage"] == "SUCCESS":
            if SaveNewUsers["responseBody"] == "Failure!!:Make sure this UserID exist On Billing Program":
                response["success"] = False
                response["status"] = 408 # user doesn't exit in the billing database
                response["msg"] = SaveNewUsers["responseBody"]
            elif SaveNewUsers["responseBody"] == "Username or password  exist Try Deffrent UserID and UserName":
                response["success"] = False
                response["status"] = 409 # user already exists
                response["msg"] = SaveNewUsers["responseBody"]

            else:
                response["success"] = True
                response["msg"] = SaveNewUsers["responseBody"]
            
        else:
            response["success"] = False
            response["status"] = 500 # server error
            response["msg"] = "Something went wrong while saving new user!!!"

        return JsonResponse(response)
        
        

    else:
        # return HttpResponseBadRequest()
        return render(request, "layout/handle_errors/handle_400.html", status=400)
    












def UpdateCustChange(request):
    if request.is_ajax():


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
                    "CGS": request.POST["CGS"],
                    "Discrip": request.POST["Descrip"],
                    "Userid": request.session.get("loggin_user")["userid"],
                    "AutoTran": 0,
                    "TranType": request.POST["TranType"],
                    "RemCentre": request.session.get("loggin_user")["UserCenter"]

                    }
            }

        print("the data of UpdateCustChange = ", data)



        headers = {
            "Authorization": request.session.get("token_type") + " " + request.session.get("access_token")
        }
    
        response = {}
        UpdateCustChange_url = 'http://192.168.2.19:96/api/values/UpdateCustChange'
        UpdateCustChange = requests.post(  UpdateCustChange_url, json=data, headers = headers)
        UpdateCustChange = json.loads(UpdateCustChange.text)

        print("the UpdateCustChange = ",UpdateCustChange)

        if UpdateCustChange["responseHeader"]["resultMessage"] == "SUCCESS":
            if UpdateCustChange["responseBody"] == "Failure!!:Make sure this UserID exist On Billing Program":
                response["success"] = False
                response["status"] = 408 # user doesn't exit in the billing database
                response["msg"] = UpdateCustChange["responseBody"]
            elif UpdateCustChange["responseBody"] == "Username or password  exist Try Deffrent UserID and UserName":
                response["success"] = False
                response["status"] = 409 # user already exists
                response["msg"] = UpdateCustChange["responseBody"]

            else:
                response["success"] = True
                response["msg"] = UpdateCustChange["responseBody"]
            
        else:
            response["success"] = False
            response["status"] = 500 # server error
            response["msg"] = "Something went wrong while changin the customer!!!"

        return JsonResponse(response)
        
        

    else:
        # return HttpResponseBadRequest()
        return render(request, "layout/handle_errors/handle_400.html", status=400)
    


    