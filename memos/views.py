from django.shortcuts import render
from .models import memos
from datetime import date
from layout.views import get_all_drivers
from notifications.views import get_all_notifications
from notifications.views import get_count
from django.http import JsonResponse

# Create your views here.
def get_memos(request):
    all_memos = memos.objects.all().order_by("-created_at")
    count = memos.objects.filter(created_at__date=date.today()).count()

    context = {
        "users": get_all_drivers(),
        "memos": all_memos,
        "memos_count": count,
        "notifications":get_all_notifications(request.user.id),
        "notification_count": get_count(request.user.id)
    }
    return render(request, "memos/memos.html", context)


def save_memos(request):
    memo = memos()
    memo.createdby_id = request.user.id
    memo.memo = request.POST["memo"]
    response = {}
    if memo.save() is None:
        response["success"] = True
        response["msg"] = "Memo successfully saved"
    else:
        response["success"] = False
        response["msg"] = "Something went wrong while saving memo"

    return JsonResponse(response)


def delete_memo(request):
    if request.method == "POST":
        response = {}
        if memos.objects.get(id=request.POST["id"]).delete():
            response["success"] = True  
            response["msg"] = "Memo is deleted successfully"  
        else:
            response["success"] = False  
            response["msg"] = "Memo delete failed"  
        return JsonResponse(response)

