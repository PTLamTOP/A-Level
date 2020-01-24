from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from cart.cart import Cart
from .models import Order, OrderItem, ReturnRequest

from django.views.generic import ListView, CreateView, View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from datetime import datetime, timedelta
import pytz

from django.contrib import messages


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'orders/order/create.html'
    fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
    extra_context = {}

    def get_success_url(self):
        return render(self.request, 'orders/order/created.html', self.extra_context)

    def get_context_data(self, **kwargs):
        cart = Cart(self.request)
        context = super().get_context_data(**kwargs)
        context.update({'cart': cart})
        return context

    def form_valid(self, form):
        user = self.request.user
        cart = Cart(self.request)
        form.instance.buyer = user
        order = form.save()
        self.extra_context.update({'order': order})
        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
            # уменьшаем деньги у пользователя и кол-во товрара на складе
            user.wallet -= (item['price'] * item['quantity'])
            user.save()
            product = item['product']
            product.stock -= item['quantity']
            product.save()
        # очистка корзины
        cart.clear()
        return self.get_success_url()


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order/list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(buyer=self.request.user)
        return queryset


class DeleteOrderItemView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = OrderItem
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        order_item = self.get_object()
        buyer = order_item.order.buyer
        product = order_item.product
        cost = order_item.price * order_item.quantity
        # return money
        buyer.wallet += cost
        buyer.save()
        # add to stock again
        product.stock += order_item.quantity
        product.save()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('orders:returns-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        order = self.object.order
        self.object.delete()
        if not order.items.all():
            order.delete()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class DeleteReturnRequestView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ReturnRequest
    http_method_names = ['post']

    def get_success_url(self):
        return reverse_lazy('orders:returns-list')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class CreateReturnView(LoginRequiredMixin, View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        order_item = OrderItem.objects.get(id=self.kwargs['order_id'])
        order_created_time = order_item.order.created
        return_valid_time = order_created_time + timedelta(days=3)
        if datetime.now(tz=pytz.UTC) > return_valid_time:
            messages.error(request, f"Sorry, you could return an order only before {return_valid_time}")
            return redirect('orders:ordered-list')
        return_request = ReturnRequest()
        return_request.item = order_item
        return_request.save()
        return redirect('orders:ordered-list')


class ReturnListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = ReturnRequest
    context_object_name = 'returns'
    template_name = 'orders/return/list.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False