from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to the task management system project.</h1>")

def contact_view(request):
    return HttpResponse("This is the contact page. Reach us at contact@taskmangement.com")

def about_view(request):
    return HttpResponse("About Us: This is the Task Management System where you can manage your tasks effectively.")

def services_view(request):
    return HttpResponse("Our Services: Task Scheduling, Progress Tracking, and Team Collaboration.")