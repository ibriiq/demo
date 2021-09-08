from django.contrib.auth.backends import UserModel
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from .decorators import Already_authenticated_users_arenot_allowed, Only_once_login_is_passed
import json

import random
import requests


@Already_authenticated_users_arenot_allowed
def ccare_login(request):
    try:
        del request.session["user"]
        del request.session["facode"]
    except KeyError:
        print(KeyError)

    if request.method == "GET":
        next = request.GET.get('next')
        context = {}
        if next is not None:
            context = {"next": next}
        return render(request, "users/login.html", context)
    else:
        if request.is_ajax():
            response = {}
            user = request.POST["username"]
            passw = request.POST["password"]

            data = {
                "requestId": "01bd2631-1a82-42b5-8e9d-5ae0c51d72cb",
                "schemaVersion": "1.0",
                "requestHeader": {
                    "timestamp": "20201126101346",
                    "apikey": "APICCAre",
                    "apiPassword": "0013801971c69437e3130b7cffd2c04cb17ca659"
                },
                "requestBody": {
                    "uid": request.POST["username"],
                    "Password": request.POST["password"]

                }
            }

            login_url = "http://192.168.2.19:96/api/values/login"
            login = requests.post( login_url, json=data)
            login = json.loads(login.text)

            if len(login["responseBody"]) > 0:

                print("the login ",login["responseBody"][0]["key"])

                request.session['facode'] = login["responseBody"][0]["key"]
                request.session["user"] = {
                    'UserName': login["responseBody"][0]["UserName"],
                    'userid': login["responseBody"][0]["userid"],
                    'FullName': login["responseBody"][0]["FullName"],
                    'UserCenter': login["responseBody"][0]["UserCenter"],
                    'UserStatus': login["responseBody"][0]["UserStatus"],
                    'BalGroups': login["responseBody"][0]["BalGroups"],
                    'AllowToViewRestrictedBalGrps': login["responseBody"][0]["AllowToViewRestrictedBalGrps"],
                    'EmployeeID': login["responseBody"][0]["EmployeeID"],
                    'MobileNo': login["responseBody"][0]["MobileNo"],
                    'MobileNo': login["responseBody"][0]["MobileNo"],
                    }

                response["success"] = True
                response["msg"] = "Loggedin successfully"
                response["redirect"] = "/2fa"
                response["next"] = request.POST["next"]

            else:
                response["success"] = False
                response["msg"] = "Invalid credentials please check the filled form!"

         

            return JsonResponse(response)

        else:
            return HttpResponseBadRequest


@Only_once_login_is_passed
def fa2(request):
    if request.method == "GET":
        next = request.GET.get('next')
        context = {}
        if next is not None:
            context = {"next": next}
        return render(request, "users/2fa.html", context)
    else:
        if request.is_ajax():
            response = {}
            code = request.POST["2fa"]

            if int(code) == int(request.session["facode"]):
               

                request.session["loggin_user"] = request.session["user"]
                # request.session.set_expiry(10)


                # token
                token_url = "http://192.168.2.19:96/token"
                data = "grant_type=password&username=ccareapiadmin@golis.so&password=Gls@#$%_12"
                token = requests.post(token_url, data)
                token = json.loads(token.text)
                request.session["access_token"] = token["access_token"]
                request.session["token_type"] = token["token_type"]





                response["success"] = True
                response["msg"] = "Loggedin successfully"
                if request.POST["next"] != "":
                    response["next"] = request.POST["next"]
                    response["redirect"] = "/"
                else:
                    response["redirect"] = "/"
                    response["next"] = ""

                try:
                    del request.session["user"]
                    del request.session["facode"]
                except KeyError:
                    print(
                        'An exception while deleting the user and the facode session keys')

            else:
                response["success"] = False
                response["msg"] = "Invalid 2fa code please check the filled form!"
                response["redirect"] = ""

            return JsonResponse(response)

        else:
            return HttpResponseBadRequest


def ccare_logout(request):
    logout(request)

    try:
        del request.session["access_token"]
        del request.session["token_type"]
    except:
        print('An exception occurred')

    return redirect("ccare_login")
