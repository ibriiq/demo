from demo.settings import DEBUG
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('cars', login_required(views.cars), name='cars'),
    path('get_cars', login_required(views.get_cars), name='get_cars'),
    path('save_cars', login_required(views.save_cars), name='save_cars'),
    path('del_car', login_required(views.del_car), name='del_car'),

    
    
    # path('get_usinfo', login_required(views.get_usinfo), name='get_usinfo'),
] 

