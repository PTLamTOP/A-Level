from django.urls import path
from .views import HallCreateView, HallListView, HallUpdateView

app_name = 'halls'

urlpatterns = [
    path('create/', HallCreateView.as_view(), name='hall-create'),
    path('', HallListView.as_view(), name='hall-list'),
    path('<int:pk>/update/', HallUpdateView.as_view(), name='hall-update'),
]
