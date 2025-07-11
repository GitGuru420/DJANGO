from django.urls import path
from tasks.views import manager_dashboard, user_dashboard, footer, home

urlpatterns = [
    path('manager-dashboard/', manager_dashboard),
    path('user-dashboard/', user_dashboard),
    path('footer/', footer),
    path('home/', home),
]