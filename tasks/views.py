from django.shortcuts import render
from .models import Tasks
from cars.models import Cars
from django.http import JsonResponse
from django.contrib.auth.models import User
from users.models import memos
import datetime
from datetime import date
from notifications.views import insert_notification
from layout.views import send_notifications, get_all_drivers
from notifications.views import get_count, get_all_notifications
from asgiref.sync import sync_to_async
from background_task import background
import pusher



# Create your views here.


    
def tasks(request):
    count = memos.objects.filter(created_at__date=date.today()).count()
    # user = User.objects.all()
    
    
    # task_title = "<a href='#' data-pk="+str(task.id)+" data-title='"+str(task.title)+"' data-start_date= '"+ str(task.start_date) +"' data-end_date= '"+ str(task.end_date) +"' data-assigned_to = "+str(task.assigned_to)+"  data-status_id =  "+str(task.status)+" class='update_tasks'>"+ str(task.title) +"</a>"
        
    context = {"users": get_all_drivers(), "memos_count": count, "notifications":get_all_notifications(request.user.id),"notification_count": get_count(request.user.id)}
    return render(request,"tasks/index.html", context)

def get_tasks(request):
    all_tasks = Tasks.objects.all()
    tasks_list = []
    sup_sn = 1
    nor_sn = 1

    for task in all_tasks:
        if task.status == 0:
            status = "To do"
        elif task.status == 1:
            status = "In progress"
        elif task.status == 2:
            status = "Done"
        if request.user.is_superuser:
            task_title = "<a href='#' data-pk="+str(task.id)+" data-title='"+str(task.title)+"' data-start_date= '"+ str(task.start_date) +"' data-end_date= '"+ str(task.end_date) +"' data-assigned_to = "+str(task.assigned_to)+"  data-status_id =  "+str(task.status)+" data-task_time = "+str(task.time)+" data-task_start_timer = "+ str(task.start_timer) +" data-task_end_timer = "+ str(task.end_timer) +"  class='update_tasks'>"+ str(task.title) +"</a>"
            action = "<a href='#' data-id='"+str(task.id)+"' class='delete_tasks' style='color: red'>  <i class='fas fa-trash-alt'></i> </a>"
            tasks_list.append({ "sn": sup_sn, "title":task_title, "start_date" : task.start_date, "end_date": task.end_date, "assigned_to": User.objects.get(id=task.assigned_to).username, "status": status,"actions": action, "time": task.time})
            sup_sn += 1
        else:
            # task_title = task.title
            task_title = "<a href='#' data-pk="+str(task.id)+" data-title='"+str(task.title)+"' data-start_date= '"+ str(task.start_date) +"' data-end_date= '"+ str(task.end_date) +"' data-assigned_to = "+str(task.assigned_to)+"  data-status_id =  "+str(task.status)+" data-task_time = "+str(task.time)+" data-task_start_timer = "+ str(task.start_timer) +" data-task_end_timer = "+ str(task.end_timer) +"  class='update_tasks'>"+ str(task.title) +"</a>"
            if task.assigned_to == request.user.id:
                tasks_list.append({ "sn": nor_sn, "title":task_title, "start_date" : task.start_date, "end_date": task.end_date, "assigned_to": User.objects.get(id=task.assigned_to).username, "status": status, "time": task.time})
                nor_sn += 1
    return JsonResponse(tasks_list, safe=False)

def get_tasks_status(request):
    response = {}
    task = Tasks.objects.get(id=request.POST["task_id"])
    if task.start_timer is not None:
        response["started"] = True
    return JsonResponse(response)


# @sync_to_async
def save_tasks(request):
    if request.method == "POST":
        task = Tasks()
        if "pk" in request.POST and request.POST["pk"] != "":
            task.pk = request.POST["pk"]
        task.title = request.POST["title"]
        task.start_date = request.POST["start_date"]
        task.end_date = request.POST["end_date"]
        task.assigned_to = request.POST["assigned_to"]
        task.status = request.POST["task_status"]
        task.time = request.POST["time"]

        response = {}
        if task.save() is None:
            notif = insert_notification(request.POST["assigned_to"], "you have been assigned new task "+str(request.POST["title"]), 1,  task.id)
            send_notifications(request, request.POST["assigned_to"])
            print(notif)
            response["success"] = True
            response["msg"] = "Successfully added new task"
        else:
            response["success"] = False
            response["msg"] = "Error while adding new task"
        return JsonResponse(response)

def del_task(request):
    if request.method == "POST":
        response = {}
        if Tasks.objects.get(id=request.POST["id"]).delete():
            response["success"] = True  
            response["msg"] = "Task successfully deleted"  
        else:
            response["success"] = False  
            response["msg"] = "Task delete failed"  
        return JsonResponse(response)



def start_timer(request):
    response = {}
    task = Tasks.objects.get(id=request.POST['task_id'])
    task.start_timer = datetime.datetime.now().time()
    task.save()
    response["success"] = True
    response["msg"] = "T0ask started"
    admin_users_list = []
    users = User.objects.filter(is_superuser=True)
    for user in users:
        admin_users_list.append(user.id)
    
    print("the admins are = ", admin_users_list)

    if task.time is None:
        end_task(request.POST['task_id'], admin_users_list, schedule=60)
    else:
        date_time = datetime.datetime.strptime(str(task.time), "%H:%M:%S")
        print(date_time)
        a_timedelta = date_time - datetime.datetime(1900, 1, 1)
        seconds = a_timedelta.total_seconds()
        print(int(seconds))
        end_task(request.POST['task_id'], admin_users_list ,schedule=(int(seconds)))
    return JsonResponse(response)


@background(schedule=60)
def end_task(task_id, admin_users_list):
    response = {}
    task = Tasks.objects.get(id=task_id)
    task.end_timer = datetime.datetime.now().time()
    task.save()

    pusher_client = pusher.Pusher(
        app_id=u'1294975',
        key=u'61de2249dc4b0a22ea49',
        secret=u'8617afcf4c5bfa8df458',
        cluster=u'ap2',
        # ssl=True
    )

    response["success"] = True
    response["msg"] = task.title+" has ended"

    for admin in admin_users_list: 
        pusher_client.trigger(u'my-channel', u'task_'+str(admin), response)
