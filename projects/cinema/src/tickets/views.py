from django.db.models import Count
from django.shortcuts import redirect

from filmsessions.models import FilmSession
from .models import Ticket

from django.views.generic import ListView, View

from django.contrib.auth.mixins import LoginRequiredMixin
from .tests import NotAdminTestMixin


class TicketsListView(LoginRequiredMixin, NotAdminTestMixin, ListView):
    """
    Display list of all users' tickets per session for an authorized user.
    """
    model = Ticket
    template_name = 'tickets/ticket/list.html'
    context_object_name = 'tickets'
    total_cost = 0

    def get_queryset(self):
        queryset = super().get_queryset().filter(buyer=self.request.user)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        # select all sessions with the users' tickets and count tickets per session using annotate()
        user_sessions = FilmSession.objects.filter(tickets__buyer=self.request.user).\
            annotate(num_tickets=Count('tickets'))
        context.update({'buyer_sessions': user_sessions})
        return context


class TicketCreate(LoginRequiredMixin, NotAdminTestMixin, View):
    """
    Authorized user can buy tickets for a session if there are enough available seats.
    """
    def post(self, request, *args, **kwargs):
        session_obj = FilmSession.objects.get(id=request.POST.get('session_id'))
        quantity = int(request.POST.get('quantity'))

        # check if there are enough available seats
        if session_obj.has_enough_seats(quantity=quantity, request=request):
            # update profile.total_cost
            request.user.profile.total_cost += (quantity * session_obj.price)
            request.user.profile.save()
            # update session.available_seats
            session_obj.available_seats -= quantity
            session_obj.update()
            # create ticket objects
            for q in range(quantity):
                ticket = Ticket(buyer=request.user, session=session_obj)
                ticket.save()
        return redirect('film-sessions:session-list')
