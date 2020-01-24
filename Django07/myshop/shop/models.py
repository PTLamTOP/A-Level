from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product-detail',
                       args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def quantity_is_enough(self, cart, data):
        product_in_cart = cart.cart.get(str(self.id))
        if product_in_cart is None or data['update']:
            if self.stock >= data['quantity']:
                return True
            return False
        quantity_in_cart = product_in_cart.get('quantity')
        if self.stock >= (data['quantity'] + quantity_in_cart):
            return True
        return False

    def money_is_enough(self, cart, user, data):
        cart_total_cost = cart.get_total_price()
        additional_cost = self.price * data['quantity']
        if data['update']:
            if user.wallet >= additional_cost:
                return True
        elif user.wallet >= (cart_total_cost + additional_cost):
            return True
        return False

