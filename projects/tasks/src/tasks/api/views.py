from tasks.models import Card
from tasks.api.serializer import CardSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .exceptions import NotAllowedData, NotAllowedStatus, NotAllowedMethod
from .permissions import IsOwnerOrReadOnly


class CardRetrieveViewSet(viewsets.ModelViewSet):
    """
    Serializer for retrieving Requests
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', ]
    permission_classes = [IsAuthenticated & IsOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        """
        Standard user can create a card only with status "NEW".
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj_data = serializer.validated_data
        if not request.user.is_superuser and obj_data['status'] != 'NW':
            raise NotAllowedData
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Standard user can update only field: 'text', 'status' from 'IP' <-> 'RD'.
        Admin can update only fields: 'text', 'executor' and 'status' from 'RD' <-> 'DN'.
        """
        card_obj = Card.objects.get(pk=kwargs['pk'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj_data = serializer.validated_data
        user_valid_statuses = ['IP', 'IQ', 'RD', ]
        admin_valid_statuses = ['RD', 'DN', ]

        if not request.user.is_superuser:
            if obj_data['status'] != card_obj.status:
                if not obj_data['status'] in user_valid_statuses:
                    raise NotAllowedStatus

            if not obj_data['executor'] == card_obj.executor or obj_data['executor'] != request.user:
                raise NotAllowedData
            if not obj_data['creator'] == card_obj.creator:
                raise NotAllowedData

        elif request.user.is_superuser:
            if obj_data['status'] != card_obj.status:
                if not obj_data['status'] in admin_valid_statuses:
                    raise NotAllowedStatus

            if not obj_data['creator'] == card_obj.creator:
                raise NotAllowedData
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise NotAllowedMethod
        return super().destroy(request, *args, **kwargs)