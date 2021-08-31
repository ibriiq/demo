from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
# Create your views here.

@login_required
def dashboard(request):
    return render(request, "layout/index.html")

def handle_400(request,exception,template_name='layout/handle_errors/handle-400.html'):
    return render(request,template_name)

def handle_404(request,exception,template_name='layout/handle_errors/handle-404.html'):
    return render(request,template_name)

def handle_500(request,exception,template_name='layout/handle_errors/handle-500.html'):
    return render(request,template_name)
