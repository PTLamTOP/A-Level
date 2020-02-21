from filmsessions.api.serializer import FilmSessionSerializer, FilmSerializer
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from filmsessions.api.permissions import IsAdminOrReadOnly

from filmsessions.models import FilmSession, Film
from filmsessions.api.filter import FilmSessionFilter

from rest_framework.response import Response
from rest_framework import status


class FilmViewSet(viewsets.ModelViewSet):
    """
    Serializer for Film's CRUD. Only admin has access.
    """
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [IsAuthenticated & IsAdminUser]


class FilmSessionViewSet(viewsets.ModelViewSet):
    """
    Serializer for FilmSession's CRUD. Admin has all accesses, standard user can only read.
    """
    queryset = FilmSession.objects.all()
    serializer_class = FilmSessionSerializer
    filter_class = FilmSessionFilter
    permission_classes = [IsAuthenticated & IsAdminOrReadOnly]

    def create(self, request, *args, **kwargs):
        """
        Session will be created if conditions below are True:
            1) if end time of new session > it's start time;
            2) if session will be in the film's screening period;
            3) if new session will not be at the same time as another existing session in the same hall.
        """
        # new session's data from API
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj_data = serializer.validated_data

        time_from = obj_data.get('time_from')
        time_to = obj_data.get('time_to')
        film_obj = obj_data.get('film')
        hall_obj = obj_data.get('hall')
        # retrieving all sessions which will be in the same hall as new session
        all_hall_sessions = FilmSession.objects.filter(hall=hall_obj)

        if FilmSession.create_session_validation(request=request, time_from=time_from,
                                                 time_to=time_to, film_obj=film_obj,
                                                 all_hall_sessions=all_hall_sessions):
            return super().create(request, *args, **kwargs)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        Session will be updated if conditions below are True:
            1) if a ticket was not purchased for the session;
            2) if end time of new session > it's start time;
            3) if session will be in the film's screening period;
            4) if new session will not be at the same time as another existing session in the same hall.
        """
        # getting the session object from DB before updating
        session_obj = FilmSession.objects.get(pk=kwargs['pk'])
        # new session's data from API
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj_data = serializer.validated_data
        time_from = obj_data.get('time_from')
        time_to = obj_data.get('time_to')
        film_obj = obj_data.get('film')
        hall_obj = obj_data.get('hall')
        # retrieving all sessions which will be in the same hall as new session, excluding the updating session
        all_hall_sessions = FilmSession.objects.filter(hall=hall_obj).exclude(id=session_obj.id)
        if session_obj.update_validate():
            if FilmSession.create_session_validation(request=request, time_from=time_from,
                                                     time_to=time_to, film_obj=film_obj,
                                                     all_hall_sessions=all_hall_sessions):
                return super().update(request, *args, **kwargs)

