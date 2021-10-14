from django.contrib.auth.backends import UserModel
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from .decorators import Already_authenticated_users_arenot_allowed, Only_once_login_is_passed
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from .models import userinfo
import json

import random
import requests


@Already_authenticated_users_arenot_allowed
def demo_login(request):
    # try:
    #     del request.session["user"]
    #     del request.session["facode"]
    # except KeyError:
    #     print(KeyError)

    if request.method == "GET":
        next = request.GET.get('next')
        context = {}
        if next is not None:
            context = {"next": next}
        return render(request, "users/login.html", context)
    else:
        if request.is_ajax():
            response = {}
            userid = request.POST["username"]
            passw = request.POST["password"]

            print(userid, passw)

            user = authenticate(username=userid, password=passw)

            if user is not None:
                login(request, user)
                response["success"] = True
                response["msg"] = "Loggedin successfully"
                response["redirect"] = "/"
                response["next"] = request.POST["next"]

            else:
                response["success"] = False
                response["msg"] = "Invalid credentials please check the filled form!"

            return JsonResponse(response)

        else:
            return HttpResponseBadRequest

def demo_logout(request):
    logout(request)

    try:
        del request.session["access_token"]
        del request.session["token_type"]
    except:
        print('An exception occurred')

    return redirect("demo_login")


def register(request):
    if request.user.is_superuser:
        if request.method == "GET":
            print(get_client_ip(request))

            return render(request, "users/register.html")
        else:
            response = {}
            user = User()
            user.first_name = request.POST["fname"]
            user.last_name = request.POST["lname"]
            user.email = request.POST["email"]
            user.username = request.POST["username"]
            user.set_password(request.POST["password"])
            # user.password = request.POST["password"]

            if User.objects.filter(email=request.POST["email"]).exists():
                response["success"] = False
                response["key"] = "email"
                response["msg"] = "email already exists in the system please use another email"
            elif User.objects.filter(username=request.POST["username"]).exists():
                response["success"] = False
                response["key"] = "username"
                response["msg"] = "username already exists in the system please use another username"
            else:
                if user.save() is None:
                    response["success"] = True
                    response["msg"] = "User registred successfully"
                else:
                    response["success"] = False
                    response["msg"] = "User registration failed"
                
        return JsonResponse(response)
    return redirect("/")


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@csrf_exempt
def save_userinfo(request):
    if request.method == "POST":
        info = userinfo()
        print(User.objects.get(username=request.POST["username"]).id)
        info.username = request.POST["username"]
        info.ip_Address = get_client_ip(request)
        info.Latitude = request.POST["Latitude"]
        info.Longitude = request.POST["Longitude"]
        response = {}
        if info.save() is None:
            response["success"] = True
        else:
            response["success"] = False
    return JsonResponse(response)


@csrf_exempt
def get_userinfo(request):
    if request.method == "POST":
        response = {}
        user = User.objects.filter(username=request.POST["username"])
        if user is not None:
            response["success"] = True
            response["data"] = {"first_name": user.first_name }
        else:
            response["success"] = False
    return JsonResponse(response)

        

