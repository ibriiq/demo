from django.shortcuts import render
from .models import notifications
from django.http import JsonResponse
from tasks.models import Tasks
from background_task import background


# Create your views here.

def insert_notification(userid, notif, notif_type, task_id):
    notification = notifications()
    notification.userid = int(userid)
    notification.notification = notif
    notification.notification_type = notif_type
    notification.task_id = task_id;
    response = {}

    # try: 
    #     notification.save()
    #     response["success"] = True
    # except:
    #     response["success"] = False
    
    # print(response)

    notification.save()
    response["success"] = True
    
    return JsonResponse(response)

    
    
def get_notifications(user_id):
    notification = notifications.objects.filter(userid=user_id).latest("id")
    data = []
    print( "the notifications = ",  notification.task_id)
    if notification.task_id:
        task = Tasks.objects.get(id=notification.task_id)  
        notification_title = "<a href='#' data-pk="+str(task.id)+" data-title='"+str(task.title)+"' data-start_date= '"+ str(task.start_date) +"' data-end_date= '"+ str(task.end_date) +"' data-assigned_to = "+str(task.assigned_to)+"  data-status_id =  "+str(task.status)+" class='update_tasks'>"+ str(notification.notification) +"</a>"
        data = {"id": notification.id,"notification": notification_title, "task_id": notification.task_id}
        print("the currentl notify = ", data)
    return data
    # return notification

def get_all_notifications(user_id):
    notification = notifications.objects.filter(userid=user_id)
    data = []
    for notification in notification:
        try:
            task = Tasks.objects.get(id=notification.task_id)  
            if notification.status == "New":

                    
                # notif = '<div class="text-reset notification-item"  style=""> \
                #                 <div class="d-flex"> \
                #                     <div class="flex-shrink-0 me-3"> \
                #                         <div class="avatar-xs"> \
                #                             <span class="avatar-title bg-success rounded-circle font-size-16"> \
                #                                 <i class="mdi mdi-cart-outline"></i> \
                #                         </span> \
                #                         </div> \
                #                     </div> \
                #                     <div class="flex-grow-1"> \
                #                         <h6 class="mb-1">You are assigned new task</h6> \
                #                         <div class="font-size-12 text-muted"> \
                #                             <!-- <p class="mb-1"> {{ notification.notification }} </p> --> \
                #                             {{ notification.notification  | safe }} \
                #                         </div> \
                #                 </div> \
                #             </div> \
                #     </div>'



                notification_title = "<a href='#' data-notification= "+str(notification.id)+" data-pk="+str(task.id)+" data-title='"+str(task.title)+"' data-start_date= '"+ str(task.start_date) +"' data-end_date= '"+ str(task.end_date) +"' data-assigned_to = "+str(task.assigned_to)+"  data-status_id =  "+str(task.status)+" class='update_tasks'>"+ str(notification.notification) +"</a>"
            else:
                notification_title = "<a href='#' data-notification= "+str(notification.id)+" data-pk="+str(task.id)+" data-title='"+str(task.title)+"' data-start_date= '"+ str(task.start_date) +"' data-end_date= '"+ str(task.end_date) +"' data-assigned_to = "+str(task.assigned_to)+"  data-status_id =  "+str(task.status)+" class='update_tasks'>"+ str(notification.notification) +"</a>"
                
            data.append({"notification": notification_title, 'status': notification.status})
        except:
            pass
    return data

def get_count(user_id):
    count = notifications.objects.filter(userid=user_id, status="New").count()
    return count


def change_notification_status(request):
    notif = notifications.objects.get(id=request.POST["notification_id"])
    notif.status = "Seen"
    notif.save()
    return JsonResponse({"success": True})