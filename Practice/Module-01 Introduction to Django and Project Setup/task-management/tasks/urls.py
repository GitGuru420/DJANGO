from django.urls import path
from tasks.views import about_view, show_view

urlpatterns = [
    path('about-view/', about_view),
    path('show-view/', show_view),
]
