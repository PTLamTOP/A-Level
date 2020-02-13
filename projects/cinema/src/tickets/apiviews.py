from .serializer import TicketSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Ticket


class TicketViewSet(viewsets.ModelViewSet):
    """
    Serializer for creating Ticket object.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
