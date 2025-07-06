from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list_and_add, name='car_list_add'),
]