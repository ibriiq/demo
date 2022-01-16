from django.shortcuts import render
from .models import Car_request
from django.http import JsonResponse
from django.contrib.auth.models import User
from memos.models import memos
from datetime import date
from notifications.views import *
from layout.views import get_all_drivers
from django.core import serializers
from notifications.views import insert_notification, send_notification
# from users.models import Employee

# Create your views here.


def car_rides(request):
    count = memos.objects.filter(created_at__date=date.today()).count()
    user = []
    for u in User.objects.all():
        if int(u.employee.userlevel) == 1:
            user.append(u)
    context = {"users": get_all_drivers(), "all_users": user, "memos_count": count, "notifications":get_all_notifications(request.user.id),"notification_count": get_count(request.user.id)}
    return render(request,"car_rides/index.html", context)

def save_car_request(request):
    if request.method == "POST":
        car = Car_request()
        if "pk" in request.POST and request.POST["pk"] != "":
            car.pk = request.POST["pk"]
        car.requested_by = request.user.id
        car.purpose = request.POST["purpose"]
        car.description = request.POST["description"]
        car.time = request.POST["time"]
        response = {}
        saved_car = car.save()
        if saved_car is None:
            response["success"] = True
            response["msg"] = "Successfully added new car request"
            notification = insert_notification(9999, 'New car request has arrived', 1, car.id)
            send_notification(notification)
        else:
            response["success"] = False
            response["msg"] = "Error while adding you car request, PLease try agin later "
        return JsonResponse(response)




def get_car_requests(request):
    all_cars = Car_request.objects.all()
    # context = { "cars": all_cars}
    cars_list = []
    sup_sn = 1
    nor_sn = 1
    for car in all_cars:
        if request.user.is_superuser:
            car_type = "<a href='#' data-pk="+str(car.id)+" class='update_car_requests' >"+ str( User.objects.get(id=car.requested_by).get_full_name() ) +"</a>"
            action = "<a href='#' data-id='"+str(car.id)+"' class='delete_car_requests btn btn-danger'>  <i class='fas fa-trash-alt'></i> </a>"
            if car.status == 0:
                car.status = "<span style='color: red;'> <i class='far fa-times-circle'></i> </span>"
            elif car.status == 1:
                car.status = "<span style='color: green;'> <i class='fas fa-check'></i> </span>"
            else:
                action += "<a href='#' data-id='"+str(car.id)+"' class='approve_car_requests btn btn-success' style=' margin-left: 5px;'>  <i class='fas fa-check'></i> </a>"
                action += "<a href='#' data-id='"+str(car.id)+"' class='reject_car_requests btn btn-warning' style=' margin-left: 5px;'>  <i class='far fa-times-circle'></i> </a>"
            
            cars_list.append({ "sn": sup_sn, "requested_by":car_type, "purpose": car.purpose, "description": car.description, "time": car.time, "status": car.status, "actions": action})
            sup_sn += 1
        else:
            if request.user.id == car.requested_by:
                car_type = "<a href='#' data-pk="+str(car.id)+" class='update_car_requests'>"+ str( User.objects.get(id=car.requested_by).get_full_name() ) +"</a>"
                # car_type = car.car_type
                if car.status == 0:
                    car.status = "<span style='color: red;'> <i class='far fa-times-circle'></i> </span>"
                elif car.status == 1:
                    car.status = "<span style='color: green;'> <i class='fas fa-check'></i> </span>"
                cars_list.append({ "sn": nor_sn, "requested_by":car_type, "purpose": car.purpose, "description": car.description, "status": car.status, "time": car.time})
                nor_sn +=1
    return JsonResponse(cars_list, safe=False)



def get_car_request(request):
    request_car = {}
    car = Car_request.objects.get(id=request.POST["id"]) 
    if car.rejected_by:
        car.rejected_by = User.objects.get(id=car.rejected_by).get_full_name()
    if car.approved_by:
        car.approved_by = User.objects.get(id=car.approved_by).get_full_name()
        car.assigned_to = User.objects.get(id=car.assigned_to).get_full_name()
    car.status_id = car.status
    if car.status == 0:
        car.status = "Rejected"
    elif car.status == 1:
        car.status = "Approved"
    request_car = {"status": car.status,"status_id": car.status_id , "rejected_by": car.rejected_by, "approved_by": car.approved_by, "assigned_to": car.assigned_to, "reason": car.rejected_reason}
    return JsonResponse(request_car)




def delete_car_request(request):
    if request.method == "POST":
        response = {}
        if Car_request.objects.get(id=request.POST["id"]).delete():
            response["success"] = True  
            response["msg"] = "Car request successfully deleted"  
        else:
            response["success"] = False  
            response["msg"] = "Car request delete failed"  
        return JsonResponse(response)


def reject_car_request(request):
    if request.method == "POST":
        response = {}
        car_request = Car_request.objects.get(id=request.POST["id"])
        car_request.status = 0
        car_request.rejected_by = request.user.id
        car_request.rejected_reason = request.POST["reason"]
        try:
            car_request.save()
            response["success"] = True  
            response["msg"] = "Car request successfully rejected"  
            notificaiton = insert_notification(car_request.requested_by," you car request to "+ car_request.purpose +" is denied", 2, car_request.id)
            send_notification(notificaiton)
        except:
            response["success"] = False  
            response["msg"] = "Car request rejection failed"  
        return JsonResponse(response)

def approve_car_request(request):
    if request.method == "POST":
        response = {}
        car_request = Car_request.objects.get(id=request.POST["id"])
        car_request.status = 1
        car_request.approved_by = request.user.id
        car_request.assigned_to = request.POST["assigned_to"]
        try:
            car_request.save()
            response["success"] = True  
            response["msg"] = "Car request successfully approved"  
            notificaiton = insert_notification(car_request.requested_by," you car request to "+ car_request.purpose +" is approved", 2, car_request.id)
            send_notification(notificaiton)
        except:
            response["success"] = False  
            response["msg"] = "Car request rejection failed"  
        return JsonResponse(response)
