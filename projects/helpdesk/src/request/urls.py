from django.urls import path, include
from .views import RequestListView, RequestDetailView, RequestUpdateView, \
    RequestCreateView, ReRequestView, CommentCreateView, ReRequestListView, \
    RequestApproveView, RequestRefuseView, RequestDeclineView, RequestRetrieveViewSet
from rest_framework.routers import DefaultRouter

app_name = 'requests'

router = DefaultRouter()
router.register('request-serializer', RequestRetrieveViewSet)

urlpatterns = [
    path('request/create/', RequestCreateView.as_view(), name='request-create'),
    path('request/<int:pk>/<slug:slug>/', RequestDetailView.as_view(), name='request-detail'),
    path('request/<int:pk>/<slug:slug>/update', RequestUpdateView.as_view(), name='request-update'),
    path('request/<int:pk>/<slug:slug>/rerequest', ReRequestView.as_view(), name='request-rerequest'),
    path('request/<int:pk>/<slug:slug>/refuse', RequestRefuseView.as_view(), name='request-refuse'),
    path('request/<int:pk>/<slug:slug>/approve', RequestApproveView.as_view(), name='request-approve'),
    path('request/<int:pk>/<slug:slug>/delete', RequestDeclineView.as_view(), name='request-delete'),
    path('request/<int:pk>/<slug:slug>/comment/create/', CommentCreateView.as_view(), name='comment-create'),
    path('re-request/', ReRequestListView.as_view(), name='rerequest-list'),
    path('', RequestListView.as_view(), name='request-list-home'),
    path('', include(router.urls)),
]