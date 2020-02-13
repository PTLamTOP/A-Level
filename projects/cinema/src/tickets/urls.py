from django.urls import path, include
from .views import TicketCreate, TicketsListView
from .apiviews import TicketViewSet
from rest_framework.routers import DefaultRouter

app_name = 'tickets'

router = DefaultRouter()
router.register('api', TicketViewSet)

urlpatterns = [
    path('create/', TicketCreate.as_view(), name='ticket-create'),
    path('', TicketsListView.as_view(), name='ticket-list'),
    path('', include(router.urls)),
]