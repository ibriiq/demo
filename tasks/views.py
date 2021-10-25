from django.shortcuts import render
from .models import Tasks
from cars.models import Cars
from django.http import JsonResponse
from django.contrib.auth.models import User
from users.models import memos
from datetime import date

# Create your views here.


def tasks(request):
    count = memos.objects.filter(created_at__date=date.today()).count()
    user = User.objects.all()
    all_cars = Cars.objects.all()
    print(all_cars)
    all_users = []
    for car in all_cars:
        all_users.append(User.objects.get(id = car.id))
    context = {"users": all_users, "memos_count": count}
    return render(request,"tasks/index.html", context)

def get_tasks(request):
    all_tasks = Tasks.objects.all()
    tasks_list = []
    sup_sn = 1
    nor_sn = 1

    for task in all_tasks:
        if request.user.is_superuser:
            task_title = "<a href='#' data-pk="+str(task.id)+" data-title='"+str(task.title)+"' data-start_date= '"+ str(task.start_date) +"' data-end_date= '"+ str(task.end_date) +"' data-assigned_to = "+str(task.assigned_to)+" class='update_tasks'>"+ str(task.title) +"</a>"
            tasks_list.append({ "sn": sup_sn, "title":task_title, "start_date" : task.start_date, "end_date": task.end_date, "assigned_to": User.objects.get(id=task.assigned_to).username})
            sup_sn += 1
        else:
            task_title = task.title
            if task.assigned_to == request.user.id:
                tasks_list.append({ "sn": nor_sn, "title":task_title, "start_date" : task.start_date, "end_date": task.end_date, "assigned_to": User.objects.get(id=task.assigned_to).username})
                nor_sn += 1
    return JsonResponse(tasks_list, safe=False)


def save_tasks(request):
    if request.method == "POST":
        task = Tasks()
        if "pk" in request.POST and request.POST["pk"] != "":
            task.pk = request.POST["pk"]
        task.title = request.POST["title"]
        task.start_date = request.POST["start_date"]
        task.end_date = request.POST["end_date"]
        task.assigned_to = request.POST["assigned_to"]
        response = {}
        if task.save() is None:
            response["success"] = True
            response["msg"] = "Successfully added new task"
        else:
            response["success"] = False
            response["msg"] = "Error while adding new task"
        return JsonResponse(response)
