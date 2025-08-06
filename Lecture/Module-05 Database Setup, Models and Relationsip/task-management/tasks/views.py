from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")

def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

def test(request):
    names = ["Mahmud", "Ahmed", "John", "Mr. X"]
    count = 0
    for name in names:
        count += 1
    context = {
        "names" : ["Mahmud", "Ahmed", "John", "Mr. X"],
        "age" : 22,
        "count" : count
    }
    return render(request, "test.html", context)