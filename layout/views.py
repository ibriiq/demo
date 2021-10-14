from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from users.models import userinfo
# Create your views here.

def dashboard(request):
    info  = userinfo.objects.all()
    

    users = []
    for user in info:
        users.append({"username": user.username, "ip_Address": user.ip_Address, "Longitude": user.Longitude, "Latitude": user.Latitude, "time": user.time,  })
        print(user)

    context ={ "userinfo": users}

    return render(request, "layout/index.html", context)

def handle_400(request,exception,template_name='layout/handle_errors/handle-400.html'):
    return render(request,template_name)

def handle_404(request,exception,template_name='layout/handle_errors/handle-404.html'):
    return render(request,template_name)

def handle_500(request,exception,template_name='layout/handle_errors/handle-500.html'):
    return render(request,template_name)
