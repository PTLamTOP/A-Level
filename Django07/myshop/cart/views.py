from django.shortcuts import redirect, get_object_or_404, reverse

from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

from django.views.generic import TemplateView, View, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages


class CartAddView(LoginRequiredMixin, FormView):
    form_class = CartAddProductForm
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('cart:cart_detail')

    def form_valid(self, form):
        cart = Cart(self.request)
        product = get_object_or_404(Product, id=self.kwargs['product_id'])
        cd = form.cleaned_data
        if product.quantity_is_enough(cart=cart,
                                      data=cd):
            if product.money_is_enough(cart=cart,
                                       user=self.request.user,
                                       data=cd):
                cart.add(product=product,
                         quantity=cd['quantity'],
                         update_quantity=cd['update'])
                return super().form_valid(form)
        if product.quantity_is_enough(cart=cart,
                                      data=cd):
            messages.error(self.request, f"We are sorry, but you do not have enough money")
        if product.money_is_enough(cart=cart,
                                   user=self.request.user,
                                   data=cd):
            messages.error(self.request, f"We are sorry, but there are only {product.stock} items in the stock.")
        return redirect(self.request.META.get('HTTP_REFERER'))


class CartRemoveView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id=kwargs['product_id'])
        cart.remove(product)
        return redirect('cart:cart_detail')


class CartDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'cart/detail.html'

    def get_context_data(self, **kwargs):
        cart = Cart(self.request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                       'update': True})
        kwargs = super().get_context_data(**kwargs)
        kwargs.update({'cart': cart, })
        return kwargs






