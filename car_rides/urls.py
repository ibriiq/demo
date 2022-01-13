from demo.settings import DEBUG
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('car_rides', login_required(views.car_rides), name='car_rides'),
    # path('get_cars', login_required(views.get_cars), name='get_cars'),
    path('get_car_requests', login_required(views.get_car_requests), name='get_car_requests'),
    path('get_car_request', login_required(views.get_car_request), name='get_car_request'),
    path('save_car_request', login_required(views.save_car_request), name='save_car_request'),
    path('delete_car_request', login_required(views.delete_car_request), name='delete_car_request'),
    path('reject_car_request', login_required(views.reject_car_request), name='reject_car_request'),
    path('approve_car_request', login_required(views.approve_car_request), name='approve_car_request'),
    # path('get_usinfo', login_required(views.get_usinfo), name='get_usinfo'),
] 

