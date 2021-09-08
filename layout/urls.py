from ccare.settings import DEBUG
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from users.decorators import login_required




urlpatterns = [
    path('', login_required(views.dashboard), name='dashboard'),
] 

