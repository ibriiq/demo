from django.contrib.auth.backends import UserModel
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from .decorators import Already_authenticated_users_arenot_allowed, Only_once_login_is_passed
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from .models import userinfo, Employee
import json
from django.utils import timezone
from datetime import date

import random
from notifications.views import *
from layout.views import get_all_drivers
from django.forms.models import model_to_dict



@Already_authenticated_users_arenot_allowed
def demo_login(request):
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
            return render(request, "users/register.html", { "users": get_all_drivers() ,"notifications":get_all_notifications(request.user.id),"notification_count": get_count(request.user.id)})
        else:
            response = {}
            user = User()
            user.first_name = request.POST["fname"]
            user.last_name = request.POST["lname"]
            user.email = request.POST["email"]
            user.username = request.POST["username"]
            
            if request.POST["usertype"] == 0:
                user.is_superuser = True
            else: 
                user.is_superuser = False
            if 'pk' in request.POST and request.POST["pk"] != '':
                user.id = request.POST['pk']
                if request.POST["password"] != '':
                    user.set_password(request.POST["password"])
                if user.save() is None:
                    employee = Employee()
                    employee.user = user
                    employee.userlevel = request.POST["usertype"]
                    employee.save()
                    response["success"] = True
                    response["msg"] = "User registred successfully"
                else:
                    response["success"] = False
                    response["msg"] = "User registration failed"
            else:
                user.set_password(request.POST["password"])
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
                        employee = Employee()
                        employee.user = user
                        employee.userlevel = request.POST["usertype"]
                        employee.save()
                        response["success"] = True
                        response["msg"] = "User registred successfully"
                    else:
                        response["success"] = False
                        response["msg"] = "User registration failed"
            
            
            
            # user.Employee.userlevel = "driver"
            # user.password = request.POST["password"]

            
                
        return JsonResponse(response)
    return redirect("/")


def get_employees(request):
    users = []
    sn = 0
    for user in User.objects.all():
        sn = sn + 1
        action = "<a href='#' data-id='"+str(user.id)+"' class='delete_user' style='color: red'>  <i class='fas fa-trash-alt'></i> </a>"
        users.append({"sn": sn,"username": "<a href='#' class='users_model_update' data-id="+str(user.id)+"> "+str(user.username)+" </a>", "email": user.email, "fullname": user.first_name+" "+user.last_name, "actions": action})
    return JsonResponse(users, safe=False)


def delete_user(request):
    if request.method == "POST":
        response = {}
        if User.objects.get(id=request.POST["id"]).delete():
            response["success"] = True  
            response["msg"] = "user successfully deleted"  
        else:
            response["success"] = False  
            response["msg"] = "user delete failed"  
        return JsonResponse(response)


def get_employee(request):
    theuser = {}
    u = User.objects.get(id=request.POST["id"])
    
    theuser = {"id": u.id,"first_name": u.first_name, "last_name": u.last_name, "email": u.email, "username": u.username, "userlevel": u.employee.userlevel}

    return JsonResponse(theuser, safe =False)




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

        





