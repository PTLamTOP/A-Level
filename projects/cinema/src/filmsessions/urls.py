from django.urls import path, include
from .views import FilmSessionsListView, SessionCreateView, SessionUpdateView, \
    FilmCreateView
from .apiviews import FilmViewSet, FilmSessionViewSet
from rest_framework.routers import DefaultRouter


app_name = 'film-sessions'

router1 = DefaultRouter()
router1.register('api/film-session', FilmSessionViewSet)
router2 = DefaultRouter()
router2.register('api/film', FilmViewSet)

urlpatterns = [
    path('session/<int:pk>/update/', SessionUpdateView.as_view(), name='session-update'),
    path('session/create/', SessionCreateView.as_view(), name='session-create'),
    path('film/create/', FilmCreateView.as_view(), name='film-create'),
    path('', FilmSessionsListView.as_view(), name='session-list'),
    path('', include(router1.urls)),
    path('', include(router2.urls)),
]
