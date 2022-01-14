from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from users.models import userinfo
from datetime import date
from memos.models import memos
from django.http import JsonResponse
from notifications.views import get_notifications, get_all_notifications, get_count
# from pusher import Pusher
import pusher
import random
import time
from django.core import serializers
from cars.models import Cars
from django.contrib.auth.models import User
from notifications.models import notifications
from asgiref.sync import sync_to_async
from background_task import background
from tasks.models import Tasks



# Create your views here.

def get_all_drivers():
    all_cars = Cars.objects.all()
    all_users = []
    for car in all_cars:
        if User.objects.get(id = car.assigned_to) is not None:
            all_users.append(User.objects.get(id = car.assigned_to))
    return all_users

def get_drivers(request):
    all_cars = Cars.objects.all()
    all_users = []
    for car in all_cars:
        if User.objects.get(id = car.assigned_to) is not None:
            all_users.append( {"username": User.objects.get(id = car.assigned_to).username, "id": User.objects.get(id = car.assigned_to).id }) 
    return JsonResponse(all_users, safe=False)



def dashboard(request):
    if request.user.is_superuser:
        info  = userinfo.objects.all()
    else:
        info  = userinfo.objects.filter(username= request.user.username)

    
    users = []
    for user in info:
        users.append({"username": user.username, "ip_Address": user.ip_Address, "Longitude": user.Longitude, "Latitude": user.Latitude, "login_time": user.time, "logout_time": user.logout_time  })

    count = memos.objects.filter(created_at__date=date.today()).count()

    context ={"users": get_all_drivers(), "userinfo": users, "memos_count": count, "notifications":  get_all_notifications(request.user.id), "notification_count": get_count(request.user.id)}

    return render(request, "layout/index.html", context)

# @sync_to_async
def send_notifications(request, current):
    pusher_client = pusher.Pusher(
        app_id=u'1294975',
        key=u'61de2249dc4b0a22ea49',
        secret=u'8617afcf4c5bfa8df458',
        cluster=u'ap2',
        # ssl=True
    )
    data = {}
    notify  = get_notifications(current)
    count_notify  = get_count(current)
    data["notification"] = notify["notification"]
    data["count"] = count_notify
    pusher_client.trigger(u'my-channel', u'my-event_'+str(current), data)
    check_task_status(notify["id"], notify["task_id"])


@background(schedule=900)
def check_task_status(id, task_id):
    pusher_client = pusher.Pusher(
        app_id=u'1294975',
        key=u'61de2249dc4b0a22ea49',
        secret=u'8617afcf4c5bfa8df458',
        cluster=u'ap2',
        # ssl=True
    )
    users = User.objects.filter(is_superuser=True)
    task = Tasks.objects.get(id=task_id)
    for user in users:
        notification_status = notifications.objects.get(id=id)
        if notification_status.status == "New":
            pusher_client.trigger(u'my-channel', u'my-event_'+str(user.id), {"notification": "Task "+task.title+" wasn't Opened by user in 15 minutes"})





# send_notifications()

def get_usinfo(request):
    if request.user.is_superuser:
        info  = userinfo.objects.all()
    else:
        info  = userinfo.objects.filter(username= request.user.username)


    users = []
    sn = 0
    for user in info:

        if request.user.is_superuser:
            username = "<a href='#' class='toggle_usermodel' data-username= "+user.username+" data-long="+str(user.Longitude)+" data-lat=" +str(user.Latitude)+" data-bs-toggle='modal' data-bs-target='#usersmodel'>" +user.username+" </a>"
        else:
            username = user.username
        sn = sn + 1
        users.append({"sn": sn, "name": user.username, "username": username, "ip_Address": user.ip_Address, "Longitude": user.Longitude, "Latitude": user.Latitude, "login_time": str(user.time).split("T")[0].split(".")[0], "logout_time": str(user.logout_time).split("T")[0].split(".")[0] })
        
    return JsonResponse(users, safe=False)



def handle_400(request,exception,template_name='layout/handle_errors/handle-400.html'):
    return render(request,template_name)

def handle_404(request,exception,template_name='layout/handle_errors/handle-400.html'):
    return render(request,template_name)

def handle_500(request,exception,template_name='layout/handle_errors/handle-500.html'):
    return render(request,template_name)
