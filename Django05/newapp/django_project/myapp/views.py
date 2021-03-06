from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Animal, Ticket
from .forms import AnimalForm

from django.utils import timezone
from datetime import timedelta

from django.urls import reverse


class AnimalList(FormView, ListView):
    model = Animal
    template_name = 'myapp/animal_list.html'
    context_object_name = 'animals'
    extra_context = {'title': 'Animal List'}
    form_class = AnimalForm

    def __init__(self):
        self.search_results = None  # a new attribute to store search-results data
        super().__init__()

    def get_success_url(self):
        return reversed('/')

    def get(self, request, *args, **kwargs):
        # if HTTP GET request with data from from with input data name='name'
        fields = ['name', 'sex']
        if all(field in request.GET for field in fields):
            name = request.GET.get('name')  # retrieve value from key 'name' in dict GET data form
            sex = request.GET.get('sex')
            self.search_results = Animal.objects.filter(name__icontains=name, sex=sex)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_results'] = self.search_results  # add search-results in context to show search results in a template
        return context


class AnimalDetail(DetailView):
    model = Animal
    template_name = 'myapp/animal_detail.html'
    context_object_name = 'animal'
    extra_context = {'title': 'Animal Detail'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['visit_5_minutes_ago'] = context['animal'].visit_set.filter(
                                                                    visit_at__gte=timezone.now()-timedelta(minutes=5))
        return context


class AnimalCreate(LoginRequiredMixin, CreateView):
    model = Animal
    fields = ['name', 'age', 'sex', 'type']
    template_name = 'myapp/animal_create.html'
    extra_context = {'title': 'Animal Create'}

    def get_login_url(self):
        return reverse('zoo:login')


class TicketCreate(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ['age_limit']
    template_name = 'myapp/ticket_create.html'
    extra_context = {'title': 'Ticket buy'}
    success_url = '/'

    def get_login_url(self):
        return reverse('zoo:login')

    def form_valid(self, form):
        form.instance.visitor = self.request.user
        return super().form_valid(form)




class CustomLoginView(LoginView):
    template_name = 'myapp/login.html'
    login_url = 'login'
    extra_context = {'title': 'Login'}

    def get_success_url(self):
        return reverse('zoo:animal-list')


class CustomLogoutView(LogoutView):
    template_name = 'myapp/logout.html'
    extra_context = {'title': 'Logout'}








