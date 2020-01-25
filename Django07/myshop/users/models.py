from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    wallet = models.DecimalField(max_digits=10, decimal_places=2, default=10000.00)

    def __str__(self):
        return self.username

    def buy(self, price, quantity, product):
        self.wallet -= price * quantity
        self.save()
        product.stock -= quantity
        product.save()

    def refund(self, order_item):
        self.wallet += order_item.price * order_item.quantity
        self.save()
        product = order_item.product
        product.stock += order_item.quantity
        product.save()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'