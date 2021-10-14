from demo.settings import DEBUG
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from django.contrib.auth.decorators import login_required




urlpatterns = [
    path('', login_required(views.dashboard), name='dashboard'),
] 

