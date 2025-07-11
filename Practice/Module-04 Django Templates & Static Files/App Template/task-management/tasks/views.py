from django.shortcuts import render
from django.http import HttpResponse

# manager dashboard
def manager_dashboard(request):
    return render(request, "manager-dashboard.html")

# user dashboard
def user_dashboard(request):
    return render(request, "user-dashboard.html")

# footer
def footer(request):
    return render(request, "footer.html")

# home
def home(request):
    context = {
        'name' : 'Raisul Islam',
        'age' : 25,
        'friends' : ["Mansur", "Iqbal", "Sowrov"]
    }
    return render(request, "home.html", context)
