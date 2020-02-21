from django.urls import path, include
from .views import TicketCreate, TicketsListView
from tickets.api.views import TicketViewSet
from rest_framework.routers import DefaultRouter

app_name = 'tickets'

router = DefaultRouter()
router.register('api', TicketViewSet, basename='Ticket')

urlpatterns = [
    path('create/', TicketCreate.as_view(), name='ticket-create'),
    path('', TicketsListView.as_view(), name='ticket-list-home'),
    path('', include(router.urls)),
]