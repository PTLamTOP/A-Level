from datetime import datetime
import pytz

from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.contrib import messages

from .models import FilmSession, Film

from django.views.generic import ListView, CreateView, UpdateView

from .tests import AdminTestMixin


class FilmSessionsListView(ListView):
    """
    list of all sessions' which can be sorted:
        1) by date: today/tomorrow
        2) by start_time: A-Z/Z-A
        3) by price: A-Z/Z-A
    """
    model = FilmSession
    template_name = 'filmsessions/sessions/list.html'
    context_object_name = 'sessions'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.GET.getlist('sort')  # sorting data of 'start_time' and 'price'
        date_sort_str = self.request.GET.get('date')  # sorting data of date: 'today' and 'tomorrow'
        # sort the queryset by date firstly if there is date data
        if date_sort_str:
            date_sort = datetime.strptime(date_sort_str, '%Y-%m-%d')
            queryset = queryset.filter(time_from__date=date_sort)
        # sort the queryset by date secondly if there are price, start time data
        if sort:
            queryset = queryset.order_by(*sort)
        return queryset


class FilmCreateView(AdminTestMixin, CreateView):
    """
    Admin can create a new film.
    """
    model = Film
    fields = ['title', 'picture', 'genre', 'description',
              'release_year', 'period_from', 'period_to']
    template_name = 'films/film/create.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, f'The new film was created!')
        return reverse_lazy('film-sessions:session-list')


class SessionCreateView(AdminTestMixin, CreateView):
    """
    Admin can create a new session.
    """
    model = FilmSession
    fields = ('film', 'hall', 'price', 'time_from', 'time_to', )
    template_name = 'filmsessions/sessions/create.html'

    def post(self, request, *args, **kwargs):
        film_obj = Film.objects.get(id=int(request.POST.get('film')))
        hall_id = int(request.POST.get('hall'))
        all_hall_sessions = FilmSession.objects.filter(hall__id=hall_id)

        # new session's naive datetime
        time_from_str = request.POST.get('time_from')
        time_to_str = request.POST.get('time_to')
        # transform the time to aware datetime 'Europe/Kiev'
        local = pytz.timezone('Europe/Kiev')
        time_from = local.localize(datetime.strptime(time_from_str, '%Y-%m-%d %H:%M'), is_dst=True)
        time_to = local.localize(datetime.strptime(time_to_str, '%Y-%m-%d %H:%M'), is_dst=True)

        # check if end time of new session > start time AND that session will be in the film's screening period
        if FilmSession.check_valid_sessiontime(request=request, time_from=time_from,
                                               time_to=time_to, film=film_obj):
            # check if new session will not be at the same time as another existing session in the hall
            if all(s.check_time_with_session_time(request=request,
                                                  time_from=time_from,
                                                  time_to=time_to) for s in all_hall_sessions):
                messages.add_message(request, messages.SUCCESS, f'The new session was created!')
                return super().post(request, *args, **kwargs)
        return redirect(self.request.META.get('HTTP_REFERER'))

    def get_success_url(self):
        return reverse_lazy('film-sessions:session-list')


class SessionUpdateView(AdminTestMixin, UpdateView):
    """
    Admin can update a session if tickets were not purchased for the session.
    """
    model = FilmSession
    fields = ('film', 'hall', 'price', 'time_from', 'time_to', )
    template_name = 'filmsessions/sessions/update.html'
    context_object_name = 'session'

    def get_success_url(self):
        return reverse_lazy('film-sessions:session-list')

    def post(self, request, *args, **kwargs):
        session_obj = FilmSession.objects.get(pk=kwargs.get('pk'))
        # check if session does not have any ticket
        if not session_obj.tickets.all():
            messages.add_message(request, messages.SUCCESS, f'The session was updated!')
            return super().post(request, *args, **kwargs)
        messages.add_message(request, messages.ERROR, f"The session can not be updated, "
                                                      f"as a ticket was already purchased for the session!")
        return redirect(self.request.META.get('HTTP_REFERER'))



