from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, FormView
from .models import Animal
from django.utils import timezone
from datetime import timedelta
from .forms import AnimalForm

# TEST FUNCTION CREATE VIEW
"""
from .forms import AnimalForm
from django.shortcuts import redirect

def create_animal(request):
    template_name = 'blog/animal_create.html'

    if request.method == 'POST':
        form = AnimalForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AnimalForm()

    return render(request, template_name, {'title': 'Animal Create',
                                           'form': form})
"""


class AnimalList(FormView, ListView):
    model = Animal
    template_name = 'blog/animal_list.html'
    context_object_name = 'animals'
    extra_context = {'title': 'Animal List'}
    form_class = AnimalForm

    def get_success_url(self):
        return reversed('/')



class AnimalDetail(DetailView):
    model = Animal
    template_name = 'blog/animal_detail.html'
    context_object_name = 'animal'
    extra_context = {'title': 'Animal Detail'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['visit_5_minutes_ago'] = context['animal'].visit_set.filter(
                                                                    visit_at__gte=timezone.now()-timedelta(minutes=5))
        return context


class AnimalCreate(CreateView):
    model = Animal
    fields = ['name', 'age', 'sex', 'type']
    template_name = 'blog/animal_create.html'
    extra_context = {'title': 'Animal Create'}










