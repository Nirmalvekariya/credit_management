
from django.urls import path
from . import views

app_name="credits"

urlpatterns = [
    path('', views.home, name='home'),
    path('allusers/', views.allusers, name='allusers'),
    path('userdetails/<int:user_id>', views.userdetails, name='userdetails'),
    path('transfer/<int:user_id>', views.transfer, name='transfer'),

]
