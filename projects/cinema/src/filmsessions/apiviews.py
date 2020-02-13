from .serializer import FilmSessionSerializer, FilmSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import FilmSession, Film
from .filter import FilmSessionFilter

from rest_framework.response import Response
from rest_framework import status


class FilmViewSet(viewsets.ModelViewSet):
    """
    Serializer for creating Film object.
    """
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [IsAuthenticated & IsAdminUser]


class FilmSessionViewSet(viewsets.ModelViewSet):
    """
    Serializer for CRUD FilmSession objects.
    """
    queryset = FilmSession.objects.all()
    serializer_class = FilmSessionSerializer
    filter_class = FilmSessionFilter
    permission_classes = [IsAuthenticated & IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj_data = serializer.validated_data
        # new session's data from API
        time_from = obj_data.get('time_from')
        time_to = obj_data.get('time_to')
        film_obj = obj_data.get('film')
        hall_obj = obj_data.get('hall')
        # retrieving all sessions which will be in the same hall as new session
        all_hall_sessions = FilmSession.objects.filter(hall=hall_obj)
        # check if end time of new session > start time AND that session will be in the film's screening period
        # And check if new session will not be at the same time as another existing session in the hall
        if FilmSession.api_create_session_validation(request=request, time_from=time_from,
                                                     time_to=time_to, film_obj=film_obj,
                                                     all_hall_sessions=all_hall_sessions):
            return super().create(request, *args, **kwargs)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        session_obj = FilmSession.objects.get(pk=kwargs['pk'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj_data = serializer.validated_data
        # new session's data from API
        time_from = obj_data.get('time_from')
        time_to = obj_data.get('time_to')
        film_obj = obj_data.get('film')
        hall_obj = obj_data.get('hall')
        # retrieving all sessions which will be in the same hall as new session, excluding the updating session
        all_hall_sessions = FilmSession.objects.filter(hall=hall_obj).exclude(id=session_obj.id)
        # check if session does not have any ticket
        if session_obj.api_update_validate():
            # check if end time of new session > start time AND that session will be in the film's screening period
            # And check if new session will not be at the same time as another existing session in the hall
            if FilmSession.api_create_session_validation(request=request, time_from=time_from,
                                                         time_to=time_to, film_obj=film_obj,
                                                         all_hall_sessions=all_hall_sessions):
                return super().update(request, *args, **kwargs)