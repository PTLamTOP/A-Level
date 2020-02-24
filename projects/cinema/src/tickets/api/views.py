from .serializer import TicketSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadAndBuyOnly

from tickets.models import Ticket
from filmsessions.models import FilmSession

from tickets.api.exceptions import NotAvailableTicket


class TicketViewSet(viewsets.ModelViewSet):
    """
    Serializer for creating Ticket object.
    """
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated & IsAdminOrReadAndBuyOnly]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Ticket.objects.all()
        return self.request.user.tickets.all()

    def perform_create(self, serializer):
        session_id = self.request.data.get('session')
        session_obj = FilmSession.objects.get(id=session_id)
        user = self.request.user
        if session_obj.available_seats == 0:
            raise NotAvailableTicket
        # update user profile.total_cost value
        user.profile.total_cost += session_obj.price
        user.save()
        # update session.available_seats value
        session_obj.available_seats -= 1
        session_obj.update()
        serializer.save(buyer=self.request.user)

