from django.urls import path
from .views import AnimalList, AnimalDetail, AnimalCreate, \
    CustomLoginView, CustomLogoutView, TicketCreate

app_name = 'zoo'

urlpatterns = [
    path('', AnimalList.as_view(), name='animal-list'),
    path('animal/<int:pk>', AnimalDetail.as_view(), name='animal-detail'),
    path('new-animal/', AnimalCreate.as_view(), name='animal-create'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('buy-ticket/', TicketCreate.as_view(), name='ticket-buy'),
]