from django.db import models
from shop.models import Product
from django.conf import settings

from datetime import datetime, timedelta
import pytz


class Order(models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='orders',
                              null=True,
                              blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    is_returned = models.CharField(max_length=200, default='')

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

    def return_is_valid(self):
        created_time = self.order.created
        return_valid_time = created_time + timedelta(minutes=3)
        if datetime.now(tz=pytz.UTC) <= return_valid_time:
            return True
        return False


class ReturnRequest(models.Model):
    item = models.OneToOneField(OrderItem,
                                on_delete=models.CASCADE,
                                related_name='returned_item')
    created = models.DateTimeField(auto_now_add=True)








