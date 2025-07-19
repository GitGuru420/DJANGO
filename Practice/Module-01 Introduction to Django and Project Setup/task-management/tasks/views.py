from django.shortcuts import render
from django.http import HttpResponse

# Home View
def home_view(request):
    return HttpResponse("<h1>Welcome to the Task Management System</h1>")    

# Contact View
def contact_view(request):
    return HttpResponse("<h1>This is contact page. Reach us at contact@taskmanagement.com</h1>")

# About View
def about_view(request):
    return HttpResponse("<h1>About Us: This is the Task Management System where you can manage your tasks effictively</h1>")

# Services View
def services_view(request):
    return HttpResponse("<h1>Services: This displays task details and related information</h1>")