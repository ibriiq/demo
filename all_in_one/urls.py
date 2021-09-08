from ccare.settings import DEBUG
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .all_views import xaliye, IN, options
from users.decorators import login_required

urlpatterns = [
    path('', login_required(views.all_in_one) , name = "all_in_one"),

    # xaliye urls begins here
    path('xaliye/UpdateXallyeBlacklist', login_required(xaliye.UpdateXallyeBlacklist) , name = "UpdateXallyeBlacklist"),
    path('xaliye/UpdateXallyeDisable', login_required(xaliye.UpdateXallyeDisable) , name = "UpdateXallyeDisable"),
    path('xaliye/UpdateXallyeresetbin', login_required(xaliye.UpdateXallyeresetbin) , name = "UpdateXallyeresetbin"),
    # xaliye urls ends here


     # IN urls begins here
    path('IN/iCBSWebdisClaimMissing', login_required(IN.iCBSWebdisClaimMissing) , name = "iCBSWebdisClaimMissing"),
    path('IN/iCBSWebBlacklist', login_required(IN.iCBSWebBlacklist) , name = "iCBSWebBlacklist"),
    # IN urls ends here




    # options begin here
    path('options/DisplayPhoneDirectory', login_required(options.DisplayPhoneDirectory) , name = "DisplayPhoneDirectory"),
    path('options/DisplayArea', login_required(options.DisplayArea) , name = "DisplayArea"),
    path('options/SaveSahalComp', login_required(options.SaveSahalComp) , name = "SaveSahalComp"),
    path('options/SaveNewUsers', login_required(options.SaveNewUsers) , name = "SaveNewUsers"),
    path('options/UpdateCustChange', login_required(options.UpdateCustChange) , name = "UpdateCustChange"),





    # options ends here




    
] 