from django.contrib.auth.backends import UserModel
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from .decorators import Already_authenticated_users_arenot_allowed, Only_once_login_is_passed
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from .models import userinfo, memos
import json
from django.utils import timezone
from datetime import date

import random


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
    info = userinfo.objects.filter(username=request.user.username).latest('pk')
    info.logout_time = timezone.now()
    info.save()
    logout(request)
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
            user.is_superuser = request.POST["usertype"]
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
def update_userinfo(request):
    if request.method == "POST":
        info = userinfo.objects.filter(username=request.user.username).latest("pk")
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

        



def get_memos(request):
    all_memos = memos.objects.all().order_by("-created_at")
    count = memos.objects.filter(created_at__date=date.today()).count()

    context = {
        "memos": all_memos,
        "memos_count": count
    }
    return render(request, "users/memos.html", context)


def save_memos(request):
    memo = memos()
    memo.createdby_id = request.user.id
    memo.memo = request.POST["memo"]
    response = {}
    if memo.save() is None:
        response["success"] = True
        response["msg"] = "Memo successfully saved"
    else:
        response["success"] = False
        response["msg"] = "Something went wrong while saving memo"

    return JsonResponse(response)



