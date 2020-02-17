from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Card
from .forms import CardForm

from django.views.generic import (ListView, DetailView, CreateView,
                                  View, DeleteView, UpdateView, )

from django.contrib.auth.mixins import UserPassesTestMixin


class SetYourselfAsExecutor(UserPassesTestMixin, View):
    """
    User can set yourself as an executor of his own request.
    """
    card_obj = None
    http_method_names = ('post', )

    def post(self, request, *args, **kwargs):
        self.card_obj.executor = request.user
        self.card_obj.status = 'IP'
        self.card_obj.save()
        return redirect(self.card_obj.get_absolute_url())

    def test_func(self):
        """
        Only creator of card can set himself as card's executor.
        """
        self.card_obj = Card.objects.get(pk=self.kwargs.get('pk'))
        if self.request.user == self.card_obj.creator:
            return True


class CardChangeStatusView(UserPassesTestMixin, View):
    """
    View is responsible for changing 'status' of card.
    Standard user can change status from 'In progress' <-> 'Ready'.
    Admin can change status from 'Ready' <-> 'Done'.
    """
    card_obj = None

    def post(self, request, *args, **kwargs):
        move_value = request.POST.get('move')
        if move_value == 'Next':
            move_index = 1
        else:
            move_index = -1
        if not request.user.is_superuser:
            self.card_obj.notadmin_card_status_change(request=request, move_index=move_index)
        else:
            self.card_obj.admin_card_status_change(request=request, move_index=move_index)
        return redirect(self.card_obj.get_absolute_url())

    def test_func(self):
        """
        Only admin or executor of Card object can change his status
        """
        self.card_obj = Card.objects.get(pk=self.kwargs.get('pk'))
        if self.request.user.is_superuser or self.request.user == self.card_obj.executor:
            return True


class CardUpdateView(UserPassesTestMixin, UpdateView):
    """
    View is responsible for cards' 'text' and 'executor' fields updating.
    """
    model = Card
    template_name = 'tasks/task/update.html'
    context_object_name = 'card'
    fields = ['executor', 'text', ]
    executor = None  # it is needed to save the current card's executor,
    # as standard user send only 'text' data, so form stores None object in the 'executor' field

    def form_valid(self, form):
        """
        Adding condition if Card.status == 'NEW" and admin set a executor -> change Card.status to 'In Progress'
        """
        if self.object.status == 'NW' and self.request.user.is_superuser and not form.initial.get('executor'):
            form.instance.status = 'IP'
        elif not self.request.user.is_superuser:
            form.instance.executor = self.executor
        return super().form_valid(form)

    def get_success_url(self):
        return str(self.object.get_absolute_url())

    def test_func(self):
        """
        Permissions:
            User (creator, executor) of card can update only field 'text' of Card object.
            Admin can update only fields 'text' and 'executor' of Card object.
        Tests:
            1) If HTTP POST check:
                a) if all POSTs' name fields are 'text' or 'executor'
                b) Standard user can have only field 'text' in POST data.
                c) Admin can have only 'text' and 'executor' fields in POST data.
                If all conditions are met -> update a Card object according to new data.
             2) If HTTP GET check:
                If user is admin or user is owner, or executor of a Card object can get access to update page.
        """
        card_obj = Card.objects.get(pk=self.kwargs.get('pk'))
        self.executor = card_obj.executor
        # HTTP POST
        if self.request.method == 'POST':
            valid_fields = ('text', 'executor', 'csrfmiddlewaretoken', )
            fields_in_post = self.request.POST.keys()
            if all(required_key in valid_fields for required_key in fields_in_post):
                # standard user can not send data in 'executor' field
                if not self.request.user.is_superuser:
                    if self.request.POST.get('executor'):
                        return False
                return True
        # HTTP GET
        elif self.request.user.is_superuser or \
                self.request.user == card_obj.creator or \
                self.request.user == card_obj.executor:
            return True


class CardDeleteView(UserPassesTestMixin, DeleteView):
    """
    User delete a Card object.
    """
    model = Card
    queryset = Card.objects.all()

    def get_success_url(self):
        return reverse_lazy('tasks:card-list-home')

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
