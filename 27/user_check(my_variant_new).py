"""
User class
__password = self.hash_password()
first_name
last_name
.get_fullname()
addresses = list[dict with keys "city", "country", "billing_address", "index"
phones = list[str] <= len(15), max 3
get attr _password = AccessDeniedException
.check_password(raw_password) -> bool
"""

# 1. Импортируем модуль bcrypt для работы с паролем
import bcrypt

# 2. Создаем два кастомных ошибок при попытки пользователя получить свой пароль и при внесение неправльных данных
class AccessDeniedException(Exception):
    pass

class InvalidDataProvided(Exception):
    pass

# 3. Создаем класс User по требованием выше

class User:
    # при создания класса по дефаулту указываем args и kwargs даже если их не используем
    # в конструкторе __init__ указываем через двоеточно, чтобы мы понимали какие типы данных нужны для объекта
    def __init__(
            self, password: str, first_name: str, last_name: str,
            addresses: list, phones: list, *args, **kwargs
    ):
        self.__password = self._hashed_pass(password=password)
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = self._validate_addresses(addresses=addresses)
        self. phones = self._validate_phones(phones=phones)

    # cвойства и методы работы с паролем
    @property
    # создаем свойства через @property. При попытке получить пароль, вызывается ошибка
    def password(self):
        raise AccessDeniedException("You can't access to password")

    @password.setter
    # так как @property был создан, теперь можем создавать setter для @property password
    def password(self, password):
        self.__password = self._hashed_pass(password=password)

    @staticmethod
    # создаем staticmethod для работы внутри класса для хэширования пароля
    def _hashed_pass(password):
        hashed_pasword = bcrypt.hashpw(password=password.encode("utf-8"), salt=bcrypt.gensalt())
        return hashed_pasword

    # создаем метод для сравнения пароля
    def check_password(self, raw_password):
        # endcode() перевели необработнный пароль в формат в который был преобразован текущий пароль и сравниваем
        return bcrypt.checkpw(raw_password.encode(), self.__password)

    # создаем свойства через @property для получения полного имени
    @property
    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'

    # Проверяем правильность ввода адресов
    @staticmethod
    # функция, которая проверяет отдельный адрес на правильность данных
    def _validate_address(address):
        required_keys = ["city", "billing_address", "country", "index"]
        if all(key in address for key in required_keys):
            return address
        raise InvalidDataProvided("Provide valid data")

    @classmethod
    # классовый метод, который через loop использует staticmethod выше для проверки всех адрессов
    def _validate_addresses(cls, addresses):
        if addresses and isinstance(addresses, list): # проверяем если адрес не пустой и он является списком
            return [cls._validate_address(address) for address in addresses]
        raise InvalidDataProvided("Provide valid data")

    # Проверяем правильность ввода телефона
    @staticmethod
    def _validate_phone(phone):
        if len(phone) <= 15 and isinstance(phone, str):
            return phone
        raise InvalidDataProvided("Provide valid data")

    @classmethod
    def _validate_phones(cls, phones):
        if phones and isinstance(phones, list):
            return [cls._validate_phone(phone) for phone in phones]
        raise InvalidDataProvided("Provide valid data")

    """
    Другой варинат реализации с дополнительной проверкой
    def _validate_phones(self, phones):
        if isinstance(phones, list) and len(phones) < 4 and all(
                (self._validate_phone(phone) for phone in phones)
        ):
            return phones
        raise InvalidDataProvided("Provide valid phones")
    """


# Тест
password = "prodota25"
first_name = "Lam"
last_name = "Pham Tung"
phones = ["1234567890", "0987665412", "213331313"]
invalid_phones = ["213132", "4342343", "324224224", "43422312312313213212432"]
addresses = [
    {
        "country": "Ukraine",
        "city": "Kharkov",
        "billing_address": "Test street 32, 99",
        "index": 61195
    }
]
invalid_addresses = [
    {
        "country": "Ukraine",
        "city": "Kharkov",
        "billing_address": "Test street 32, 99",
    }
]

user_1 = User(password, first_name, last_name, addresses, phones)

print(user_1.check_password('prodota25'))
print(user_1.phones)
