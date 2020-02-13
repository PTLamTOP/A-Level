from .serializer import HallSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Hall
from rest_framework import serializers


class HallViewSet(viewsets.ModelViewSet):
    """
    Serializer for creating Film object.
    """
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [IsAuthenticated & IsAdminUser]

    def update(self, request, *args, **kwargs):
        hall_obj = Hall.objects.get(pk=kwargs['pk'])
        new_seats_amount = int(request.POST.get('seats'))
        if hall_obj.can_be_update():
            for s in hall_obj.sessions.all():
                s.update_seats_amount(new_amount=new_seats_amount)
            return super().update(request, *args, **kwargs)
        raise serializers.ValidationError(f"ERROR: The hall can not be updated, "
                                                      f"as a ticket in the hall was already bought")