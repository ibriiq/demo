from django.shortcuts import render
from .models import Cars, Checklist_car
from django.http import JsonResponse
from django.contrib.auth.models import User
from memos.models import memos
from datetime import date
from notifications.views import *
from layout.views import get_all_drivers
from django.core import serializers
# from users.models import Employee

# Create your views here.


def cars(request):
    count = memos.objects.filter(created_at__date=date.today()).count()
    user = []
    for u in User.objects.all():
        if int(u.employee.userlevel) == 1:
            user.append(u)

    context = {"users": get_all_drivers(), "all_users": user, "memos_count": count, "notifications":get_all_notifications(request.user.id),"notification_count": get_count(request.user.id)}
    return render(request,"cars/index.html", context)

def get_cars(request):
    all_cars = Cars.objects.all()
    context = { "cars": all_cars}
    cars_list = []
    sup_sn = 1
    nor_sn = 1

    for car in all_cars:
        if request.user.is_superuser:
            car_type = "<a href='#' data-pk="+str(car.id)+" data-cars_type='"+str(car.car_type)+"' data-assigned_to = "+str(car.assigned_to)+" class='update_cars' >"+ str(car.car_type) +"</a>"
            action = "<a href='#' data-id='"+str(car.id)+"' class='delete_cars' style='color: red'>  <i class='fas fa-trash-alt'></i> </a>"
            cars_list.append({ "sn": sup_sn, "cars_type":car_type, "assigned_to": User.objects.get(id=car.assigned_to).username, "actions": action})
            sup_sn += 1
        else:
            if request.user.id == car.assigned_to:
                car_type = "<a href='#' data-pk="+str(car.id)+" data-cars_type='"+str(car.car_type)+"' data-assigned_to = "+str(car.assigned_to)+" class='update_cars'>"+ str(car.car_type) +"</a>"
                # car_type = car.car_type
                cars_list.append({ "sn": nor_sn, "cars_type":car_type, "assigned_to": User.objects.get(id=car.assigned_to).username})
                nor_sn +=1
    return JsonResponse(cars_list, safe=False)

def get_car(request):
    car_dict = {}
    checklist_dict = []
    cars = Cars.objects.filter(id=request.POST["id"])  


    for car in cars:
        car_dict = {
        "pk": car.id,
        "car_assigned_to": User.objects.get(id=car.assigned_to).username,
        "car_type": car.car_type, 
        "assigned_to": car.assigned_to,
        "tax_renewed_date": car.tax_renewed_date,
        "tax_expiration_date": car.tax_expiration_date,
        "fitness_renewed_date": car.fitness_renewed_date,
        "fitness_expiration_date": car.fitness_expiration_date,
        "car_maintanance_date": car.car_maintanance_date,
        "car_condition": car.car_condition
        }
    # car = serializers.serialize('json', car)
    checklists = Checklist_car.objects.filter(car_id=request.POST["id"])
    for checklist in checklists:
        checklist_dict.append({
            "title": checklist.title,
            "is_checked": checklist.is_checked
        })
    # checklist = serializers.serialize('json', checklist)
    return JsonResponse({ "car": car_dict, "checklist": checklist_dict})


def save_cars(request):
    if request.method == "POST":
        car = Cars()
        if "pk" in request.POST and request.POST["pk"] != "":
            car.pk = request.POST["pk"]
        car.car_type = request.POST["car_type"]
        car.assigned_to = request.POST["assigned_to"]
        if request.POST["car_road_renewed"] and request.POST["car_road_renewed"]  != "":
            car.tax_renewed_date = request.POST["car_road_renewed"]
        if request.POST["car_road_expire"] and request.POST["car_road_expire"]  != "":
            car.tax_expiration_date = request.POST["car_road_expire"]
        if request.POST["car_fitness_renewed"] and request.POST["car_fitness_renewed"]  != "":
            car.fitness_expiration_date =request.POST["car_fitness_renewed"]
        if request.POST["car_fitness_expire"] and request.POST["car_fitness_expire"]  != "":
            car.fitness_renewed_date =request.POST["car_fitness_expire"]
        if request.POST["car_maintenance_expire"] and request.POST["car_maintenance_expire"]  != "":
            car.car_maintanance_date =request.POST["car_maintenance_expire"]
        car.car_condition =request.POST["car_conditions"]

        response = {}
        saved_car = car.save()
        if saved_car is None:
            checklist = Checklist_car()
            checklist.car_id = car.id
            checklist.title = "Car has road Tax"
            checklist.save()

            checklist = Checklist_car()
            checklist.car_id = car.id
            checklist.title = "Car has Fitness check"
            checklist.save()

            checklist = Checklist_car()
            checklist.car_id = car.id
            checklist.title = "Car has being maintained"
            checklist.save()

            checklist = Checklist_car()
            checklist.car_id = car.id
            checklist.title = "Car has being maintained"
            checklist.save()

            checklist = Checklist_car()
            checklist.car_id = car.id
            checklist.title = "Car is in good conditions"
            checklist.save()


            response["success"] = True
            response["msg"] = "Successfully added new car"
        else:
            response["success"] = False
            response["msg"] = "Error while adding new car"
        return JsonResponse(response)



def del_car(request):
    if request.method == "POST":
        response = {}
        if Cars.objects.get(id=request.POST["id"]).delete():
            response["success"] = True  
            response["msg"] = "Cars successfully deleted"  
        else:
            response["success"] = False  
            response["msg"] = "Cars delete failed"  
        return JsonResponse(response)



def save_checklist(request):

    checklists = Checklist_car.objects.filter(car_id=request.POST["id"])
    for checklist in checklists:
        if request.POST["checklist_type"] in checklist.title:
            checklist.is_checked = request.POST["checklist"]
            checklist.save()
            
    return JsonResponse({"success": True})

