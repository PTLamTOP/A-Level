from django.urls import reverse
from django.views.generic import ListView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from .models import Article
from .forms import ArticleForm


class SearchFormView(FormView):
    form_class = ArticleForm
    template_name = 'myapp/search.html'


class ArticleListView(ListView):
    model = Article
    template_name = 'myapp/index.html'
    context_object_name = 'articles'
    ordering = ['-created_at']


class CustomLoginView(LoginView):
    template_name = 'myapp/login.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse('index')


class CustomLogoutView(LogoutView):
    template_name = 'myapp/logout.html'







"""
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


# пример реализации login в Django функциональный подход
def login_view(request):

    if request.method == 'POST':
        # .POST хранит данные отправленной формы в виде словаря
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'myapp/index.html', {'user': user})
        else:
            return HttpResponse('Login wrong data!')

    else:
        form = LoginForm()

    return render(request, 'myapp/login.html', {'form': form})


# пример реализации login в Django функциональный подход
def logout_view(request):
    logout(request)
    return render(request, 'myapp/logout.html')
"""