from django.shortcuts import render
from .models import Cars
from django.http import JsonResponse
from django.contrib.auth.models import User
from users.models import memos
from datetime import date

# Create your views here.


def cars(request):
    count = memos.objects.filter(created_at__date=date.today()).count()
    user = User.objects.all()
    context = {"users": user, "memos_count": count}
    return render(request,"cars/index.html", context)

def get_cars(request):
    all_cars = Cars.objects.all()
    context = { "cars": all_cars}
    cars_list = []
    sup_sn = 1
    nor_sn = 1

    for car in all_cars:
        if request.user.is_superuser:
            car_type = "<a href='#' data-pk="+str(car.id)+" data-cars_type='"+str(car.car_type)+"' data-assigned_to = "+str(car.assigned_to)+" class='update_cars'>"+ str(car.car_type) +"</a>"
            action = "<a href='#' data-id='"+str(car.id)+"' class='delete_cars' style='color: red'>  <i class='fas fa-trash-alt'></i> </a>"
            cars_list.append({ "sn": sup_sn, "cars_type":car_type, "assigned_to": User.objects.get(id=car.assigned_to).username, "actions": action})
            sup_sn += 1
        else:
            if request.user.id == car.assigned_to:
                car_type = car.car_type
                cars_list.append({ "sn": nor_sn, "cars_type":car_type, "assigned_to": User.objects.get(id=car.assigned_to).username})
                nor_sn +=1
    return JsonResponse(cars_list, safe=False)


def save_cars(request):
    if request.method == "POST":
        car = Cars()
        if "pk" in request.POST and request.POST["pk"] != "":
            car.pk = request.POST["pk"]
        car.car_type = request.POST["car_type"]
        car.assigned_to = request.POST["assigned_to"]
        response = {}
        if car.save() is None:
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
