from ccare.settings import DEBUG
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.all_in_one) , name = "all_in_one"),
    path('/UpdateXallyeBlacklist', login_required(views.UpdateXallyeBlacklist) , name = "UpdateXallyeBlacklist"),
] 