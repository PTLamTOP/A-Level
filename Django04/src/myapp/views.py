from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .forms import StudentForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


"""
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse('Good Job!')
        return HttpResponse('Bad Job!')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StudentForm()

    return render(request, 'myapp/index.html', {'form': form})
"""
def request(request):
    return render(request, 'myapp/request.html')

class MyFormView(FormView):
    template_name = 'myapp/index.html'
    http_method_names = ['get', 'post']
    form_class = StudentForm
    initial = {'name': 'Linda', 'sex': 'female', 'age': '13', 'english_level': '2'}

    def get(self, request, *args, **kwargs):
        print('GET REQUEST')
        return super().get(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        print('POST REQUEST')
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return HttpResponse('Good job!')

    def form_invalid(self, form):
        return HttpResponse('Bad Job!')



# пример реализации login в Django функциональный подход
def login_view(request):

    if request.method == 'POST':
        # .POST хранит данные отправленной формы в виде словаря
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'request', {'user': user})
        else:
            return HttpResponse('Login wrong data!')

    else:
        form = LoginForm()

    return render(request, 'myapp/login.html', {'form': form})


# пример реализации login в Django функциональный подход
def logout_view(request):
    logout(request)
    return render(request, 'myapp/request.html')


class CustomLoginView(LoginView):
    template_name = 'myapp/login.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse('login')


class CustomLogoutView(LogoutView):
    template_name = 'myapp/request.html'




