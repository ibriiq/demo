from demo.settings import DEBUG
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('tasks', login_required(views.tasks), name='tasks'),
    path('get_tasks', login_required(views.get_tasks), name='get_tasks'),
    path('save_tasks', login_required(views.save_tasks), name='save_tasks'),
    path('del_task', login_required(views.del_task), name='del_task'),
] 

