from django.shortcuts import render
from django.http import HttpResponse

# Home View
def home_view(request):
    return HttpResponse("<h1>Welcome to the Task Management System</h1>")

# Contact View
def contact_view(request):
    return HttpResponse("<h1>This is the contact page. Reach us at contact@taskmanagement.com</h1>")

# About View
def about_view(request):
    return HttpResponse("<h1>About US: This is the 'Task Management System' where you can manage your tasks effectively</h1>")

# Show View
def show_view(request):
    return HttpResponse("<h1>Show Task: This display task details and related information</h1>")