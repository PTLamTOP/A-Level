from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Card
from .forms import CardForm

from django.views.generic import ListView, DetailView, CreateView, \
    View, DeleteView, UpdateView

from django.contrib.auth.mixins import UserPassesTestMixin

from .serializer import CardSerializer
from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CardRetrieveViewSet(viewsets.GenericViewSet,
                             mixins.ListModelMixin):
    """
    Serializer for retrieving Requests
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', ]
    permission_classes = [IsAuthenticated & IsAdminUser]


class SetYourselfAsExecutor(UserPassesTestMixin, View):
    """
    User can set yourself as an executor of his own request.
    """
    card_obj = None

    def post(self, request, *args, **kwargs):
        self.card_obj.executor = request.user
        self.card_obj.status = 'IP'
        self.card_obj.save()
        return redirect( self.card_obj.get_absolute_url())

    def test_func(self):
        self.card_obj = Card.objects.get(pk=self.kwargs.get('pk'))
        if self.request.user == self.card_obj.creator:
            return True


class CardChangeStatusView(UserPassesTestMixin, View):
    card_obj = None

    def post(self, request, *args, **kwargs):
        move_value = request.POST.get('move')
        if move_value == 'Next':
            move_index = 1
        else:
            move_index = -1
        if not request.user.is_superuser:
            statuses = ['IP', 'IQ', 'RD']
            current_status_index = statuses.index(self.card_obj.status)
            try:
                new_status = statuses[current_status_index+move_index]
            except IndexError:
                new_status = 'RD'
            if current_status_index == 0 and move_index == -1:
                self.card_obj.status == 'NW'
            else:
                self.card_obj.status = new_status
            self.card_obj.save()
            return redirect(self.card_obj.get_absolute_url())
        # if user is super_user
        statuses = ['RD', 'DN']
        current_status_index = statuses.index(self.card_obj.status)
        try:
            new_status = statuses[current_status_index + move_index]
        except IndexError:
            new_status = 'DN'
        if current_status_index == 0 and move_index == -1:
            self.card_obj.status == 'NW'
        else:
            self.card_obj.status = new_status
        self.card_obj.save()
        return redirect(self.card_obj.get_absolute_url())

    def test_func(self):
        """
        Only admin or executor of Card object can change his status
        """
        self.card_obj = Card.objects.get(pk=self.kwargs.get('pk'))
        if self.request.user.is_superuser or self.request.user == self.card_obj.executor:
            return True


class CardUpdateView(UserPassesTestMixin, UpdateView):
    model = Card
    template_name = 'tasks/task/update.html'
    context_object_name = 'card'
    fields = ['executor', 'text']

    def form_valid(self, form):
        """
        Adding condition if Card.status == 'NEW" and admin set a executor -> change Card.status to 'In Progress'
        """
        if self.object.status == 'NW' and self.request.user.is_superuser and not form.initial.get('executor'):
            form.instance.status = 'IP'
            form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return str(self.object.get_absolute_url())

    def test_func(self):
        """
        Permissions:
            User can update only field 'text' of Card object.
            Admin can update only filed 'text' and 'executor' of Card object.
        Tests:
            1) If HTTP POST check:
                a) if all POSTs' name fields are 'text' or 'executor'
                b) Standard user can have only field 'text' in POST data.
                c) Admin can have only 'text' and 'executor' fields in POST data.
                If all conditions are met -> update a Card object according to new data.
             2) If HTTP GET check:
                If user is admin or user is owner of a Card object can get access to update page.
        """
        card_obj = Card.objects.get(pk=self.kwargs.get('pk'))
        # HTTP POST
        if self.request.method == 'POST':
            valid_fields = ('text', 'executor', 'csrfmiddlewaretoken')
            fields_in_post = self.request.POST.keys()
            if all(required_key in valid_fields for required_key in fields_in_post):
                if not self.request.user.is_superuser:
                    if self.request.POST.get('executor'):
                        return False
                return True
        # HTTP GET
        elif self.request.user.is_superuser or self.request.user == card_obj.creator:
            return True


class CardDeleteView(UserPassesTestMixin, DeleteView):
    """
    User delete a Card object.
    """
    model = Card
    queryset = Card.objects.all()

    def get_success_url(self):
        return reverse_lazy('tasks:card-list')

    def test_func(self):
        if self.request.user.is_superuser:
            return True


class CardCreateView(CreateView):
    """
    User create new Card object.
    """
    form_class = CardForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return str(self.object.get_absolute_url())


class CardListView(ListView):
    """
    List of all cards for admin and user.
    If user - show all users' cards.
    if admin - show all cards.
    """
    model = Card
    template_name = 'tasks/task/list.html'
    context_object_name = 'cards'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context.update({'card_create_form': CardForm, })
        return context


class CardDetailView(DetailView):
    model = Card
    template_name = 'tasks/task/detail.html'
    context_object_name = 'card'
