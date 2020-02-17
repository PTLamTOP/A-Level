from request.api.serializer import RequestSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from request.models import Request


class RequestRetrieveViewSet(viewsets.ModelViewSet):
    """
    Serializer for retrieving Requests
    """
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['importance', ]
    permission_classes = [IsAuthenticated & IsAdminUser]