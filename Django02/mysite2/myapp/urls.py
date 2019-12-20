from django.contrib import admin
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('<int:number>/', index, name='integer'),
    path('<str:string>/', index, name='string'),
]