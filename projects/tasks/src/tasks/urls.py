from django.urls import path, include
from .views import (CardListView, CardDetailView, CardCreateView,
                    CardDeleteView, CardUpdateView, CardChangeStatusView,
                    SetYourselfAsExecutor, )

from rest_framework.routers import DefaultRouter
from .api.views import CardRetrieveViewSet

app_name = 'tasks'

router = DefaultRouter()
router.register('api/card', CardRetrieveViewSet)

urlpatterns = [
    path('card/create/', CardCreateView.as_view(), name='card-create'),
    path('card/<int:pk>/<slug:slug>/', CardDetailView.as_view(), name='card-detail'),
    path('card/<int:pk>/<slug:slug>/update', CardUpdateView.as_view(), name='card-update'),
    path('card/<int:pk>/<slug:slug>/change-status', CardChangeStatusView.as_view(), name='card-change-status'),
    path('card/<int:pk>/<slug:slug>/become-executor', SetYourselfAsExecutor.as_view(), name='card-become-executor'),
    path('card/<int:pk>/<slug:slug>/delete', CardDeleteView.as_view(), name='card-delete'),
    path('', CardListView.as_view(), name='card-list-home'),
    path('', include(router.urls)),
]