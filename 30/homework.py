"""
ЧАСТЬ 1 (СДЕЛАЛ)
1) Есть класс товара, у которого есть свойства: имя и цена.

2) Должны существовать три вида покупателей: простой, вип, супер-вид. Каждый из них наследуется от друг друга:
простой->вип->супер->вип. У всех должен быть свойство бюджет.

У всех покупалей должен быть метод, который принимает продукт и говорит сколько продуктов может купить данный покупателель.
Скидки:
1) простой покупатель - нет скидки
2) вип покупатель - 20%
3) супер-вип покупаетль - еще 20% от скидки вип

Ошбика - https://codeday.me/ru/qa/20190920/366875.html

ЧАСТЬ 2 (СДЕЛАЛ)
Валидация:
- отрицательный бюджет и цена
- тип данных float
- проверка что передается класс продукт в методу покупателя

ЧАСТЬ 3 (СДЕЛАЛ)
наследуемся от класса Product создаем элитный класс продукт, на которого не распространяется скидка.
Шаги:

ЧАСТЬ 4 (СДЕЛАЛ)
Задать продукту скидку, которая будет брать при расчеты цены данную скидку вместо скидки покупателя.
Если скидка нет, то скидка покупателя.

ЧАСТЬ 5 (СДЕЛАЛ)
Добавить информацию о кол-ве продуктов на складе, добавить покупателям метод купить продукт(или несколько),
при покупке у клиента должен уменьшатся бюджет, а у продукта уменьшать кол-во на складе.
!!!Валидация на количество доступных продуктов на складе.

ЧАСТЬ 6 (СДЕЛАЛ)
Дописать возможность добавлять продукты на склад, и пополнять бюджет клиента
"""
# импорт класс floor из модуля math
from math import floor


# создаем кастомный класс ошибок
class InvalidData(Exception):
    pass

class NoMoney(Exception):
    pass

class NoProduct(Exception):
    pass


# Создаем класс Product
# 1) Обычный продукт:
class Product:
    def __init__(self, product_name: str, price: float, discount=0):
        self.product_name = product_name
        self.price = self._validate_price(price)
        # есть ли у продукта скидка, по умолчанию нет(0)
        self.discount = self._validate_discount(discount)
        # является ли продукт типом SUPER продукт
        self._super_product = False
        # количество продуктов на складе
        self.quantity = 20

    # пополнить кол-во продукта на склад
    def _increase_product(self, number):
        if self._validate_int(number):
            self.quantity += number
            return f'{number} {self.product_name}s were delivered to the warehouse. ' \
                   f'Current quantity is {self.quantity}.'
        raise InvalidData('Please input a number!')

    # уменьшить продукт при покупке
    def _reduce_product(self, number):
        if self._validate_int(number):
            self.quantity -= number
            return f'{number} {self.product_name}s were bought by the customer. ' \
                   f'Current quantity is {self.quantity}.'
        raise InvalidData('Please input a number!')

    def __repr__(self):
        if self._super_product:
            return f'The {self.product_name} costs {self.price} UAH. It is super product with discount of ' \
                   f'{self.discount}%. There are {self.quantity} {self.product_name}s at the warehouse.'
        return f'The {self.product_name} costs {self.price} UAH. It is standard product with discount of ' \
               f'{self.discount}%. There are {self.quantity} {self.product_name}s at the warehouse.'

    # валидация цены
    @staticmethod
    def _validate_price(price):
        # проверяет если внесенная цена: не пустой, класс float или int, больше 0
        if price and (isinstance(price, float) or isinstance(price, int)) and price > 0:
            return float(price)
        raise InvalidData('Price data is Invalid!')

    # валидация скидки
    @staticmethod
    def _validate_discount(discount):
        # проверяет если внесенная цена: не пустой, класс float или int, от 0 до 100
        if (isinstance(discount, float) or isinstance(discount, int)) and discount >= 0 and discount <= 100:
            return float(discount)
        raise InvalidData('Discount data is Invalid!')

    # валидация номера int
    @staticmethod
    def _validate_int(number):
        if number and isinstance(number, int) and number > 0:
            return number
        raise InvalidData("Please input a number!")

# 2) Super продукт:
class SuperProduct(Product):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # у Super продукта никогда нет никакой скидки
        self.has_discount = False
        self._super_product = True



# Создаем класс Customer: standard, vip, super_vip
# 1) Standard Customer:
class Customer:
    def __init__(self, name: str, budget: float):
        self.name = name
        self.budget = self._validate_money(budget)


    """
    Метод расчета цены на продукт для покупателя.
    Если на товар есть скидка, то берется цена со скидкой товара.
    В противном случае берется цена товара с учетом типа покупателя
    """
    @staticmethod
    def _get_price(product: Product):
        # Проверяем если у продукта скидка, если да, то возвращаем цену со скидкой продукта
        if product.discount:
            return product.price*(1-(product.discount/100))
        # Если скидки нет, то возвращаем обычную цену
        return product.price

    # частный метод, который расчитывает доступное кол-во продуктов, который может себе позволить покупатель
    def _allowable_amount(self, product: Product):
        return floor(self.budget/self._get_price(product))

    # метод, который выводит строку об кол-во продуктов, который может себе позволить покупатель.
    def can_buy(self, product: Product):
        # проверяет если аргумент явялется классом Product
        if isinstance(product, Product):
            return f"{self.name} can buy {self._allowable_amount(product)} {product.product_name}s with current budget."
        raise InvalidData("Please input a product!")

    """
    Метод покупки товаров покупателем.
    Если на складе меньше товаров, чем покупатель запросил, то берется количество товаров на складе при расчете.
    """
    def buy(self, basket):
        if self._validate_shopping_basket(basket):
            cost = self._cost_canlculation(basket)
            if self.budget >= cost:
                self.budget -= cost
                actual_basket = list(self._reduce_product(basket))
                return f"{self.name} could buy {actual_basket} for {cost} UAH. Current budget is {self.budget} UAH."
            raise NoMoney(f"{self.name}does not have enough money to buy!.")
        raise InvalidData('Please check if you input a product and quantity is correct!')

    # метод для пополнения бюджета
    def add_to_budget(self, money):
        if self._validate_money(money):
            self.budget += money
            return f"{self.name} fund the budget for {money} UAH. Current budget is {self.budget}"
        raise InvalidData("It is Invalid Data!")


    """
    Метод для расчета общей стоимости корзины покупателя
    Если на складе меньше товаров, чем покупатель запросил, то берется количество товаров на складе при расчете.
    """
    def _cost_canlculation(self, basket):
        cost = 0
        for element in basket:
            for product, quantity in element.items():
                if product.quantity >= quantity:
                    cost += self._get_price(product) * quantity
                else:
                    cost += self._get_price(product) * product.quantity
        return cost

    """
    Метод для уменьшение товаров на складе по покупкам в корзине покупателя.
    Если на складе меньше товаров, чем покупатель запросил, то берется количество товаров на складе при расчете.
    """
    @staticmethod
    def _reduce_product(basket):
        for element in basket:
            for product, quantity in element.items():
                if product.quantity >= quantity:
                    yield product.product_name, quantity
                    product._reduce_product(quantity)

                else:
                    yield product.product_name, product.quantity
                    product._reduce_product(product.quantity)

    """
    Валидация корзины покупателя:
    1) корзина должна быть класса list
    2) Элементы корзины должна быть класса dict
    3) Ключ dict должен быть класс Product
    4) Значение dict (количество) должен быть класс int
    """
    @staticmethod
    def _validate_shopping_basket(basket):
        # проверяем если basket класс list, если нет то вызваем ошибку
        if basket and isinstance(basket, list):
            # сначало проверяем если все элементы list - это класс dictionary, если нет то вызваем ошибку
            if all(isinstance(element, dict) for element in basket):
                # если да, то проходим через все dictionary в list
                for dictionary in basket:
                    # проверяем сначало что ключи dictionary - это класс Product, а значние - класс int,
                    # если нет то вызваем ошибку
                    if all(isinstance(product, Product) and isinstance(quantity, int) for product, quantity in
                           dictionary.items()):
                        return True
                    raise InvalidData("Wrong key or value of dict!")
            raise InvalidData("Not all elements of basket is dict!")
        raise InvalidData("Basket is not a list!")

    # валидация бюджета
    @staticmethod
    def _validate_money(budget):
        # проверяет если внесенный бюджет: не пустой, класс float или int, больше 0
        if budget and isinstance(budget, float) or (isinstance(budget, int)) and budget > 0:
            return float(budget)
        raise InvalidData("Budget data is Invalid!")


# 2) VIP Customer:
class VipCuctomer(Customer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # у этого класса есть скидка на обычные товары в размере 20%
        self.customer_discount = 0.80


    def _get_price(self, product: Product):
        # вызываем метод родителя для получения цены
        product_price = super()._get_price(product)
        if product._super_product:
            return product.price
        elif product.discount:
            return product_price
        return product_price * self.customer_discount


# 3) Super VIP Customer:
class SuperVipCuctomer(VipCuctomer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # у этого класса есть скидка на обычные товары в размере 36%
        self.customer_discount *= 0.80


    def _get_price(self, product: Product):
        product_price = super()._get_price(product)
        if product._super_product:
            return product.price
        elif product.discount:
            return product_price
        return product_price * self.customer_discount


# TEST
# создаем экземпляр Product
product_1 = Product('book', 10.0)
product_3 = Product('book with discount', 10, 50)
product_2 = SuperProduct('luxury book', 20)

# создаем экземпляр Customer
standard_customer = Customer('Standard Customer', 500)
vip_customer = VipCuctomer('Vip Customer', 500.0)
super_vip_customer = SuperVipCuctomer('Super Vip Customer', 500.0)
#
# # тестриуем свойства
# print("-----ТЕСТ ВЫЗОВА СВОЙСТВА CUSTOMER:")
# print(standard_customer.budget)
# print(vip_customer.name)
# print(super_vip_customer.name)
#
# # тестируем метод у разных покупателей
# print("-----ТЕСТ МЕТОДА CAN_BUY:")
# print("-----ПОКУПКА ОБЫЧНЫХ ПРОДУКТОВ БЕЗ СКИДКИ")
# print(standard_customer.can_buy(product_1))
# print(vip_customer.can_buy(product_1))
# print(super_vip_customer.can_buy(product_1))
# print("-----ПОКУПКА ОБЫЧНЫХ ПРОДУКТОВ СО СКИДКОЙ")
# print(standard_customer.can_buy(product_3))
# print(vip_customer.can_buy(product_3))
# print(super_vip_customer.can_buy(product_3))
# print("-----ПОКУПКА СУПЕР ПРОДУКТОВ")
# print(standard_customer.can_buy(product_2))
# print(vip_customer.can_buy(product_2))
# print(super_vip_customer.can_buy(product_2))
#
# # тестируем покупку продукта
print("-----ТЕСТ МЕТОДА BUY:")
basket_1 = [{product_1: 30}, {product_2: 5}]
basket_2 = [{product_1: 2}, {product_2: 2}, {product_3: 5}]
print(standard_customer.buy(basket_1))
print(product_1.quantity)
print(product_2.quantity)
print(standard_customer.add_to_budget(200))


# print(vip_customer.buy(product_1, 2))
# # print(vip_customer.buy(product_2, 1))
# # print(vip_customer.buy(product_3, 2))


# тестируем ощибки
# print("-----ОШИБКА ЕСЛИ НЕ ПЕРЕДАЛИ ПРАВИЛЬНЫЕ ДАННЫЕ ЦЕНЫ И БЮДЖЕТА ПРИ ИНИЦИАЛИЗАЦИИ")
# # product_test = Product('pen', '20')
# # standard_customer_test = Customer('Peter', '100')
# print("-----ОШИБКА ЕСЛИ АРГУМЕНТ НЕ ЯВЛЯЕТСЯ КЛАССОМ PRODUCT")
# print(standard_customer.can_buy(vip_customer))
# print(standard_customer.buy(product_1, -2))
# print(standard_customer.buy(product_1, 0))
# print(standard_customer.buy(product_1, 100))
