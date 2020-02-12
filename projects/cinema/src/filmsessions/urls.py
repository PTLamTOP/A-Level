from django.urls import path, include
from .views import FilmSessionsListView, SessionCreateView, SessionUpdateView, \
    FilmSessionRetrieveViewSet, FilmCreateView
from rest_framework.routers import DefaultRouter

app_name = 'film-sessions'

router = DefaultRouter()
router.register('film-session-serializer', FilmSessionRetrieveViewSet)

urlpatterns = [
    path('session/<int:pk>/update/', SessionUpdateView.as_view(), name='session-update'),
    path('session/create/', SessionCreateView.as_view(), name='session-create'),
    path('film/create/', FilmCreateView.as_view(), name='film-create'),
    path('', FilmSessionsListView.as_view(), name='session-list'),
    path('', include(router.urls)),
]
