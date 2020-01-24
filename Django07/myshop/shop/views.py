from django.shortcuts import reverse

from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from .models import Product
from cart.forms import CartAddProductForm


class ProductListView(ListView):
    model = Product
    template_name = 'shop/product/list.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'cart_product_form': CartAddProductForm})
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product/detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'cart_product_form': CartAddProductForm})
        return context


class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    fields = ['name', 'image', 'description', 'price', 'stock', 'available']
    template_name = 'shop/product/create.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['name', 'image', 'description', 'price', 'stock', 'available']
    template_name = 'shop/product/update.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product

    def get_success_url(self):
        return reverse('shop:product_list')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


