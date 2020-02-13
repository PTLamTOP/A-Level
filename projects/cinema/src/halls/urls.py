from django.urls import path, include
from .views import HallCreateView, HallListView, HallUpdateView
from .apiviews import HallViewSet
from rest_framework.routers import DefaultRouter

app_name = 'halls'

router = DefaultRouter()
router.register('api', HallViewSet)

urlpatterns = [
    path('create/', HallCreateView.as_view(), name='hall-create'),
    path('', HallListView.as_view(), name='hall-list'),
    path('<int:pk>/update/', HallUpdateView.as_view(), name='hall-update'),
    path('', include(router.urls)),
]
