from django.contrib import admin
from django.urls import path
from .views import index, string_button, integer_button

urlpatterns = [
    path('', index, name='index'),
    path('<int:number>/', integer_button, name='integer'),
    path('<str:string>/', string_button, name='string'),
]