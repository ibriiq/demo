from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from users.models import userinfo
from datetime import date
from users.models import memos
from django.http import JsonResponse
# Create your views here.

def dashboard(request):
    if request.user.is_superuser:
        info  = userinfo.objects.all()
    else:
        info  = userinfo.objects.filter(username= request.user.username)


    users = []
    for user in info:
        users.append({"username": user.username, "ip_Address": user.ip_Address, "Longitude": user.Longitude, "Latitude": user.Latitude, "login_time": user.time, "logout_time": user.logout_time  })
        print(user)

    count = memos.objects.filter(created_at__date=date.today()).count()

    context ={ "userinfo": users, "memos_count": count}

    print("the count is ", count)

    return render(request, "layout/index.html", context)

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
        users.append({"sn": sn, "username": username, "ip_Address": user.ip_Address, "Longitude": user.Longitude, "Latitude": user.Latitude, "login_time": str(user.time).split("T")[0].split(".")[0], "logout_time": str(user.logout_time).split("T")[0].split(".")[0] })
        print(user)

    return JsonResponse(users, safe=False)



def handle_400(request,exception,template_name='layout/handle_errors/handle-400.html'):
    return render(request,template_name)

def handle_404(request,exception,template_name='layout/handle_errors/handle-404.html'):
    return render(request,template_name)

def handle_500(request,exception,template_name='layout/handle_errors/handle-500.html'):
    return render(request,template_name)
