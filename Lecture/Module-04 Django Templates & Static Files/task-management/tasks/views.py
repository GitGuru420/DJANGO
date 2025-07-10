from django.shortcuts import render
from django.http import HttpResponse

def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")

def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

def test(request):
    names = ["Mahmud", "Ahmed", "John", "Jaqob"]
    count = 0
    for name in names:
        count += 1
    context = {
        "names" : ["Mahmud", "Ahmed", "John", "Jaqob"],
        "age" : 23,
        "count" : count,
    }
    return render(request, "test.html", context)