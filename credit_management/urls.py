
from django.contrib import admin
from django.urls import path, include
from credits import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('credits.urls')),
]
