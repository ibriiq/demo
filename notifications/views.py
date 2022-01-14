from django.shortcuts import render
from car_rides.models import Car_request
from .models import notifications
from django.http import JsonResponse
from tasks.models import Tasks
from background_task import background
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
import pusher
from datetime import datetime
import json


# Create your views here.

def insert_notification(userid, notif, notif_type, task_id):
    notification = notifications()
    notification.userid = int(userid)
    notification.notification = notif
    notification.notification_type = notif_type
    notification.task_id = task_id;
    notification.time = datetime.now()
    response = {}
    notification.save()
    response["success"] = True
    
    return notification.id

    
    
def get_notifications(user_id):
    notification = notifications.objects.filter(userid=user_id).latest("id")
    data = []
    if notification.task_id:
        task = Tasks.objects.get(id=notification.task_id)  
        notification_title = "<a href='#' data-pk="+str(task.id)+" data-title='"+str(task.title)+"' data-start_date= '"+ str(task.start_date) +"' data-end_date= '"+ str(task.end_date) +"' data-assigned_to = "+str(task.assigned_to)+"  data-status_id =  "+str(task.status)+" class='update_tasks'>"+ str(notification.notification) +"</a>"
        data = {"id": notification.id,"notification": notification_title, "task_id": notification.task_id}
    return data
    # return notification

def get_all_notifications(user_id):
    user = User.objects.get(id=user_id)
    if user.is_superuser:
        notification = notifications.objects.filter(userid=9999)
    else:
        notification = notifications.objects.filter(userid=user_id)

    data = []
    for notification in notification:
        print("the notifcations = ", notification.notification_type)
        try:
            if notification.notification_type == 0:
                task = Tasks.objects.get(id=notification.task_id)  
                if notification.status == "New":
                    notification_title = "<a href='#' data-notification= "+str(notification.id)+" data-pk="+str(task.id)+" data-title='"+str(task.title)+"' data-start_date= '"+ str(task.start_date) +"' data-end_date= '"+ str(task.end_date) +"' data-assigned_to = "+str(task.assigned_to)+"  data-status_id =  "+str(task.status)+" class='update_tasks'>"+ str(notification.notification) +"</a>"
                else:
                    notification_title = "<a href='#' data-notification= "+str(notification.id)+" data-pk="+str(task.id)+" data-title='"+str(task.title)+"' data-start_date= '"+ str(task.start_date) +"' data-end_date= '"+ str(task.end_date) +"' data-assigned_to = "+str(task.assigned_to)+"  data-status_id =  "+str(task.status)+" class='update_tasks'>"+ str(notification.notification) +"</a>"
                data.append({"notification": notification_title, 'status': notification.status})
            elif notification.notification_type == 1:
                task = Car_request.objects.get(id=notification.task_id)  
                if notification.status == "New":
                    request_notificaiton =    '<a href="javascript:void(0);" data-notification_id= '+str(notification.id)+' class="notification_item dropdown-item notify-item">\
                                                    <div class="notify-icon bg-warning">\
                                                        <i class="mdi mdi-account-plus"></i>\
                                                    </div>\
                                                    <p class="notify-details">'+str(notification.notification)+'\
                                                        <small class="text-muted">' + str( datetime.now() - (notification.time))  + ' ago </small>\
                                                    </p>\
                                                </a>'
                data.append({"notification": request_notificaiton})
            elif notification.notification_type == 2:
                task = Car_request.objects.get(id=notification.task_id)  
                if notification.status == "New":
                    request_notificaiton =    '<a href="javascript:void(0);" data-notification_id= '+str(notification.id)+' class="notification_item dropdown-item notify-item">\
                                                    <div class="notify-icon bg-warning">\
                                                        <i class="mdi mdi-account-plus"></i>\
                                                    </div>\
                                                    <p class="notify-details">'+str(notification.notification)+'\
                                                        <small class="text-muted">' + str( datetime.now() - (notification.time))  + ' ago </small>\
                                                    </p>\
                                                </a>'




                    # notification_title = "<a href='#' data-notification= "+str(notification.id)+" data-pk="+str(task.id)+" data-title='"+str(task.title)+"' data-start_date= '"+ str(task.start_date) +"' data-end_date= '"+ str(task.end_date) +"' data-assigned_to = "+str(task.assigned_to)+"  data-status_id =  "+str(task.status)+" class='update_tasks'>"+ str(notification.notification) +"</a>"
                # else:
                    # notification_title = "<a href='#' data-notification= "+str(notification.id)+" data-pk="+str(task.id)+" data-title='"+str(task.title)+"' data-start_date= '"+ str(task.start_date) +"' data-end_date= '"+ str(task.end_date) +"' data-assigned_to = "+str(task.assigned_to)+"  data-status_id =  "+str(task.status)+" class='update_tasks'>"+ str(notification.notification) +"</a>"
                data.append({"notification": request_notificaiton})
        except:
            pass

    print(data)

    return data

def get_count(user_id):
    if  int(user_id) == 9999 or (User.objects.get(id=user_id) is not None and User.objects.get(id=user_id).is_superuser):
        count = notifications.objects.filter(userid=9999, status="New").count()
    else:
        count = notifications.objects.filter(userid=user_id, status="New").count()
    return count


def change_notification_status(request):
    notif = notifications.objects.get(id=request.POST["notification_id"])
    notif.status = "Seen"
    notif.save()
    return JsonResponse({"success": True})

def send_notification(object_id):
    notification = notifications.objects.get(id=object_id)
    pusher_client = pusher.Pusher(
        app_id=u'1294975',
        key=u'61de2249dc4b0a22ea49',
        secret=u'8617afcf4c5bfa8df458',
        cluster=u'ap2',
    )
    data = {}
    count_notify  = get_count(notification.userid)
    data["notification"] =  model_to_dict(notification)
    data["count"] = count_notify
    data = json.dumps(data, indent=4, sort_keys=True, default=str)

    if int(notification.userid) == 9999:
        users = User.objects.filter(is_superuser=True)
        for user in users:
            pusher_client.trigger(u'my-channel', u'my-event_'+str(user.id), data)
    else:
        user =  User.objects.get(id=notification.userid)
        pusher_client.trigger(u'my-channel', u'my-event_'+str(user.id), data)


    
    