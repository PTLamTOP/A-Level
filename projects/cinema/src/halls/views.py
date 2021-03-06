from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.contrib import messages

from .models import Hall

from django.views.generic import ListView, CreateView, UpdateView

from .mixins import AdminTestMixin
from halls.api.exceptions import NotAllowedToUpdate


class HallListView(AdminTestMixin, ListView):
    """
    Only admin can see the list of all halls.
    """
    model = Hall
    template_name = 'halls/hall/list.html'
    context_object_name = 'halls'


class HallCreateView(AdminTestMixin, CreateView):
    """
    Only Admin can create a new hall.
    """
    model = Hall
    fields = ('name', 'seats', )
    template_name = 'halls/hall/create.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, f'The hall was created!')
        return reverse_lazy('halls:hall-list-home')


class HallUpdateView(AdminTestMixin, UpdateView):
    """
    Only Admin can update a hall object.
    The hall can only be updated only if tickets to the hall were purchased.

    Situations:
        1. Tickets were not purchased:
            1) update the hall object
            2) update attribute 'available_seats' of all sessions which will be in the hall.

        2. Tickets were purchased -> redirect to hall's url with messages like 'Can not update the hall'
    """
    model = Hall
    fields = ('name', 'seats', )
    template_name = 'halls/hall/update.html'
    context_object_name = 'hall'

    def get_success_url(self):
        return reverse_lazy('halls:hall-list-home')

    def post(self, request, *args, **kwargs):
        hall_obj = Hall.objects.get(pk=kwargs.get('pk'))
        new_seats_amount = int(request.POST.get('seats'))
        try:
            # check if tickets to the hall were not purchased.
            hall_obj.can_be_update()
            # updated attribute 'available_seats' of all sessions in the hall
            for s in hall_obj.sessions.all():
                s.update_seats_amount(new_amount=new_seats_amount)
            messages.add_message(request, messages.SUCCESS, 'The hall was updated!')
            return super().post(request, *args, **kwargs)
        except NotAllowedToUpdate:
            messages.add_message(request, messages.ERROR, "The hall can not be updated, "
                                                          "as a ticket was already purchased for a hall's session!")
            return redirect(hall_obj.get_absolute_url())