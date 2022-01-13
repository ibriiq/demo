from demo.settings import DEBUG
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from notifications.views import change_notification_status
from django.contrib.auth.decorators import login_required




urlpatterns = [
    path('', login_required(views.dashboard), name='dashboard'),
    path('get_usinfo', login_required(views.get_usinfo), name='get_usinfo'),
    path('change_notification_status', login_required(change_notification_status), name='change_notification_status'),
    path('get_drivers', login_required(views.get_drivers), name='get_drivers'),
] 

