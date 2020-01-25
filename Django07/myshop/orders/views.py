from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from cart.cart import Cart
from .models import Order, OrderItem, ReturnRequest

from django.views.generic import ListView, CreateView, View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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
            product = item['product']
            price = item['price']
            quantity = item['quantity']
            OrderItem.objects.create(order=order,
                                     product=product,
                                     price=price,
                                     quantity=quantity)
            # decrease money of user and amount of the product in stock
            user.buy(price=price,
                     quantity=quantity,
                     product=product)
        # clean cart
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
    """
    Class view is responsible for deleting OrderItem if admin approve return
    """
    model = OrderItem
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        order_item = self.get_object()
        buyer = order_item.order.buyer
        buyer.refund(order_item=order_item)
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('orders:returns-list')

    def delete(self, request, *args, **kwargs):
        """
        Redefined the method to call self.object.delete() and check if Order is empty before self.get_success_url().

        """
        self.object = self.get_object()
        order = self.object.order
        self.object.delete()
        # if Order object does not have OrderItem (empty Order) -> delete Order
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

    def delete(self, request, *args, **kwargs):
        return_request = self.get_object()
        order_item = return_request.item
        order_item.is_returned = 'Your previous return request was denied by admin.'
        order_item.save()
        return super().delete(request, *args, **kwargs)

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
        if not order_item.return_is_valid():
            messages.error(request, f"Sorry, it is too late to return the order item.")
            return redirect('orders:ordered-list')
        order_item.is_returned = 'It is reviewing by admin. Please wait.'
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