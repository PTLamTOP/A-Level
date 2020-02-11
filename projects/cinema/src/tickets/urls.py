from django.urls import path
from .views import TicketCreate, TicketsListView

app_name = 'tickets'

urlpatterns = [
    path('create/', TicketCreate.as_view(), name='ticket-create'),
    path('', TicketsListView.as_view(), name='ticket-list'),
]