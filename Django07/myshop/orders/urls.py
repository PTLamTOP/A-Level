from django.urls import path
from .views import OrderListView, CreateReturnView, OrderCreateView, \
    ReturnListView, DeleteOrderItemView, DeleteReturnRequestView

app_name = 'orders'

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order-create'),
    path('list/', OrderListView.as_view(), name='ordered-list'),
    path('<int:order_id>/return/create/', CreateReturnView.as_view(), name='return-create'),
    path('returns-list/', ReturnListView.as_view(), name='returns-list'),
    path('order-item/<int:pk>/delete/', DeleteOrderItemView.as_view(), name='order-item-delete'),
    path('return-request/<int:pk>/delete/', DeleteReturnRequestView.as_view(), name='return-request-delete'),
]