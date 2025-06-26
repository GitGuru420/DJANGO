from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the task-management system")

def name(request):
    return HttpResponse("<h1>My name is Raisul Islam</h1>")

def university(request):
    return HttpResponse("<h1 style='color: red'>SMUCT</h1>")