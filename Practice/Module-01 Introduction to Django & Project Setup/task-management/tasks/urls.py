from django.urls import path
from tasks.views import about_view, services_view

urlpatterns = [
    path('about/', about_view),
    path('services/', services_view),
]
