from .serializer import TicketSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadAndBuyOnly

from tickets.models import Ticket


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
        serializer.save(buyer=self.request.user)