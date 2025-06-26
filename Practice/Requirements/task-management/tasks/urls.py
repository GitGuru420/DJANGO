from django.urls import path
from tasks.views import university

urlpatterns = [
    path('university/', university),
]