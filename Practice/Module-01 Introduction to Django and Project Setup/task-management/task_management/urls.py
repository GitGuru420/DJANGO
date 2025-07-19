from django.contrib import admin
from django.urls import path, include
from tasks.views import home_view, contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('contact/', contact_view),
    path('tasks/', include('tasks.urls')),
]
