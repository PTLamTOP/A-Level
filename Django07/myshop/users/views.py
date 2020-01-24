from django.shortcuts import render, reverse

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from .forms import AuthorRegisterForm


class RegistrationView(CreateView):
    template_name = 'users/user/register.html'
    http_method_names = ['get', 'post']
    form_class = AuthorRegisterForm

    def get_success_url(self):
        return reverse('users:login')


class MyLoginView(LoginView):
    template_name = 'users/user/login.html'


class MyLogoutView(LogoutView):
    template_name = 'users/user/logout.html'



