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

            user = authenticate(username=user, password=passw)

            print("the user is ", user)

            if user is not None:
                # login(request, user)
                # randomly generated 2fa codes
                facode = random.randrange(1, 100000)
                # phone = user.user_profile.phone
                phone = "907022730"
                url = "http://192.168.2.13:14013/cgi-bin/sendsms?username=sms_guure&password=Sms_local&to=" + \
                    str(phone)+"&from=CCare&text=Your%20CCare%20access%20code%20is%20:%20" + \
                    str(facode)+"&mclass=0"
                requests.get(url)
                request.session['facode'] = facode
                request.session["user"] = {
                    'username': user.username, "pk": user.pk}

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
                user = UserModel.objects.get(
                    username=request.session["user"]["username"])
                login(request, user)

                token_url = "http://192.168.2.19:96/token"

                data = "grant_type=password&username=ccareapiadmin@golis.so&password=Gls@#$%_12"

                token = requests.post(token_url, data)
                token = json.loads(token.text)

                request.session["access_token"] = token["access_token"]
                request.session["token_type"] = token["token_type"]

                response["success"] = True
                response["msg"] = "Loggedin successfully"
                if request.POST["next"] is not "":
                    response["next"] = request.POST["next"]
                    response["redirect"] = ""
                else:
                    response["redirect"] = "/dashboard"
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
