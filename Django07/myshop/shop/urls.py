from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView


app_name = 'shop'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:id>/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/create/', ProductCreateView.as_view(), name='product-create'),
    path('product/update/<int:id>/<slug:slug>/', ProductUpdateView.as_view(), name='product-update'),
    path('product/delete/<int:id>/<slug:slug>/', ProductDeleteView.as_view(), name='product-delete'),
]