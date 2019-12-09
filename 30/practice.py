# Создали класс Product
class Product:
    def init(self, name, cost):
        self.name = name
        self._cost = cost

    def get_price_off(self):
        return self._cost * 0.8

    @property
    def cost(self):
        return self.get_price_off()


class SuperPriceOffProduct(Product):

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)

    def get_price_off(self):
        current_price = super().get_price_off()
        return current_price * 0.9


p1 = Product(name='milk', cost=100)
p2 = SuperPriceOffProduct(name='bread', cost=200)
print(p1.get_price_off())
print(p2.get_price_off())
print(p1.cost)
print(p2.cost)