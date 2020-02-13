from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.contrib import messages

from .models import Hall

from django.views.generic import ListView, CreateView, UpdateView

from .tests import AdminTestMixin


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
        return reverse_lazy('halls:hall-list')


class HallUpdateView(AdminTestMixin, UpdateView):
    """
    Only Admin can update a hall object.
    The hall can only be updated only if tickets to the hall were purchased.

    Situations:
        1. Tickets were not purchased:
            1) update the hall object
            2) update attribute 'available_seats' of all sessions which will be in the hall.

        2. Tickets were purchased -> redirect to 'HTTP_REFERER' with messages like 'Can not update the hall'
    """
    model = Hall
    fields = ('name', 'seats', )
    template_name = 'halls/hall/update.html'
    context_object_name = 'hall'

    def get_success_url(self):
        return reverse_lazy('halls:hall-list')

    def post(self, request, *args, **kwargs):
        hall_obj = Hall.objects.get(pk=kwargs.get('pk'))
        new_seats_amount = int(request.POST.get('seats'))
        if hall_obj.can_be_update():  # check if tickets to the hall were not purchased.
            for s in hall_obj.sessions.all():  # updated attribute 'available_seats' of all sessions in the hall
                s.update_seats_amount(new_amount=new_seats_amount)
            messages.add_message(request, messages.SUCCESS, f'The hall was updated!')
            return super().post(request, *args, **kwargs)
        messages.add_message(request, messages.ERROR, f"The hall can not be updated, "
                                                      f"as a ticket in the hall was already bought")
        return redirect(self.request.META.get('HTTP_REFERER'))