from django.db.models import Count
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.contrib import messages

from .models import FilmSession, Film, Hall, Ticket

from django.views.generic import ListView, CreateView, UpdateView, View

from datetime import datetime
import pytz

from .serializer import FilmSessionSerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .filter import FilmSessionFilter


class FilmSessionRetrieveViewSet(viewsets.GenericViewSet,
                                 mixins.ListModelMixin):
    """
    Serializer for retrieving Requests
    """
    queryset = FilmSession.objects.all()
    serializer_class = FilmSessionSerializer
    filter_class = FilmSessionFilter
    permission_classes = [IsAuthenticated & IsAdminUser]


class TicketsListView(ListView):
    model = Ticket
    template_name = 'tickets/ticket/list.html'
    context_object_name = 'tickets'
    total_cost = 0

    def get_queryset(self):
        queryset = super().get_queryset().filter(buyer=self.request.user)
        for t in queryset:
            self.total_cost += t.session.price
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context.update({'total_cost': self.total_cost})
        user_sessions = FilmSession.objects.filter(tickets__buyer=self.request.user).\
            annotate(num_tickets=Count('tickets'))
        context.update({'buyer_sessions': user_sessions})
        return context


class TicketCreate(View):
    def post(self, request, *args, **kwargs):
        session_obj = FilmSession.objects.get(id=self.request.POST.get('session_id'))
        quantity = int(self.request.POST.get('quantity'))
        if session_obj.available_seats > 0 and session_obj.available_seats >= quantity:
            messages.add_message(request, messages.INFO, f'You have bought {quantity} tickets.')
            for q in range(quantity):
                ticket = Ticket(buyer=self.request.user, session=session_obj)
                ticket.save()
                session_obj.available_seats -= 1
                session_obj.update()
        elif session_obj.available_seats == 0:
            messages.add_message(request, messages.ERROR, f'Sorry, there is not any ticket.')
        else:
            messages.add_message(request, messages.ERROR, f'Sorry, there are only {session_obj.available_seats} tickets.')
        return redirect('film-sessions:session-list')


class FilmSessionsListView(ListView):
    """
    list of all sessions'.
    """
    model = FilmSession
    template_name = 'filmsessions/sessions/list.html'
    context_object_name = 'sessions'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.GET.getlist('sort')
        date_sort_str = self.request.GET.get('date')
        if date_sort_str:
            date_sort = datetime.strptime(date_sort_str, '%Y-%m-%d')
            queryset = queryset.filter(time_from__date=date_sort)
        if sort:
            queryset = queryset.order_by(*sort)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)

        return context


class FilmCreateView(CreateView):
    model = Film
    fields = ['title', 'picture', 'genre', 'description',
              'release_year', 'period_from', 'period_to']
    template_name = 'films/film/create.html'

    def get_success_url(self):
        return reverse_lazy('film-sessions:session-list')


class HallListView(ListView):
    """
    list of all halls'.
    """
    model = Hall
    template_name = 'halls/hall/list.html'
    context_object_name = 'halls'


class HallCreateView(CreateView):
    model = Hall
    fields = ('name', 'seats', )
    template_name = 'halls/hall/create.html'

    def get_success_url(self):
        return reverse_lazy('film-sessions:session-list')


class HallUpdateView(UpdateView):
    model = Hall
    fields = ('name', 'seats', )
    template_name = 'halls//hall/update.html'
    context_object_name = 'hall'

    def get_success_url(self):
        return reverse_lazy('film-sessions:hall-list')

    def post(self, request, *args, **kwargs):
        hall_obj = Hall.objects.get(pk=kwargs.get('pk'))
        hall_sessions = hall_obj.sessions.all()
        # проверяем чтобы по сеансам в данном зале не было билетов
        if all(not s.tickets.all() for s in hall_sessions):
            # также по всем сеансам место количество доступных мест на новое значение в зале
            for s in hall_sessions:
                s.available_seats = int(request.POST.get('seats'))
                s.save()
            return super().post(request, *args, **kwargs)
        # билеты есть, то просто редиректим и показываем сообщение
        messages.add_message(request, messages.ERROR, f"ERROR: Hall can not be updated, as ticket in the hall was already bought")
        return redirect(self.request.META.get('HTTP_REFERER'))


def time_valid(time_from, time_to, s):
    if (time_from < s.time_from and time_to < s.time_from) or (time_from > s.time_to and time_to > s.time_to):
        return True
    return False


class SessionCreateView(CreateView):
    model = FilmSession
    fields = ('film', 'hall', 'price', 'time_from', 'time_to', )
    template_name = 'filmsessions/sessions/create.html'

    def post(self, request, *args, **kwargs):
        time_from_str = request.POST.get('time_from')
        time_to_str = request.POST.get('time_to')
        hall_id = int(request.POST.get('hall'))

        local = pytz.timezone('Europe/Kiev')
        time_from = local.localize(datetime.strptime(time_from_str, '%Y-%m-%d %H:%M'), is_dst=True)
        time_to = local.localize(datetime.strptime(time_to_str, '%Y-%m-%d %H:%M'), is_dst=True)

        all_sessions = FilmSession.objects.filter(hall__id=hall_id)
        if time_to > time_from:
            if all(time_valid(time_from=time_from, time_to=time_to, s=s) for s in all_sessions):
                return super().post(request, *args, **kwargs)
            else:
                messages.add_message(request, messages.ERROR, f'ERROR: Session was not created, as there is already a session at this time: {time_from}-{time_to}.')
                return redirect(self.request.META.get('HTTP_REFERER'))
        else:
            messages.add_message(request, messages.ERROR, f"ERROR: Session was not created, as session's start time is less/equal than end time.")
            return redirect(self.request.META.get('HTTP_REFERER'))

    def get_success_url(self):
        return reverse_lazy('film-sessions:session-list')


class SessionUpdateView(UpdateView):
    model = FilmSession
    fields = ('film', 'hall', 'price', 'time_from', 'time_to', )
    template_name = 'filmsessions/sessions/update.html'
    context_object_name = 'session'

    def get_success_url(self):
        return reverse_lazy('film-sessions:session-list')

    def post(self, request, *args, **kwargs):
        session_obj = FilmSession.objects.get(pk=kwargs.get('pk'))
        if not session_obj.tickets.all():
            return super().post(request, *args, **kwargs)
        # билеты есть, то просто редиректим и показываем сообщение
        messages.add_message(request, messages.ERROR, f"ERROR: Session can not be updated, as ticket was already bought to the session")
        return redirect(self.request.META.get('HTTP_REFERER'))



