from django.urls import path
from .views import MyLoginView, MyLogoutView, RegistrationView

app_name = 'users'

urlpatterns =[
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
]
