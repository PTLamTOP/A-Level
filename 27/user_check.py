import bcrypt
"""
Модуль для хэширования пароля bcrypt:
tutorial - http://zetcode.com/python/bcrypt/

"""

# CREATING ERROR
# класс ошибки при попытке получения пароля
class AccessDeniedException(Exception):
    """
    Exception when user try to get password
    """


# класс ошибок по телефону
class IncorrectPhones(Exception):
    """
    Exception when user input phones not as list
    """


class PhonesMoreThan3(IncorrectPhones):
    """
    Exception when user input more than 3 phones
    """


class PhoneLengthMoreThan15(IncorrectPhones):
    """
    Exception when user input phone more than 15 symbols
    """


# класс ошибок адресса
class IncorrectAddress(Exception):
    """
    Exception when user input address not as list
    """


class IncorrectAddressDictElem(IncorrectAddress):
    """
    Exception when user input address not as dict
    """

# CREATING CLASS USER
class User:
    def __init__(self, password, name, lastname, addresses, phones, *args, **kwargs):
        self._password = self.hashed_pass(password=password)
        self.name = name
        self.last_name = lastname
        self.args = args
        self.kwargs = kwargs
        self.salt = bcrypt.gensalt()

        # Проверка валидности адресса
        if isinstance(addresses, list):
            if all(isinstance(address, dict) for address in addresses):
                self.addresses = addresses
            else:
                raise IncorrectAddressDictElem('One of address is not in dict format.')
        else:
            raise IncorrectAddressDictElem('Addresses is not as a list.')
        # Проверка валидности номера телефона
        if isinstance(phones, list):  # проверка если данные телефона является list
            if len(phones) <= 3:  # проверка если количество телефонов меньше или равно 3
                if all(len(phone) <= 15 for phone in phones):
                    self.phones = phones
                else:
                    raise PhoneLengthMoreThan15('Incorrect phone\'s format. Please check!')
            else:
                raise PhonesMoreThan3('Too much phones. Please input less than 3 phones.')
        else:
            raise IncorrectPhones('Please input phones as a list!')

    # Метод, который показывает имя и фамилию пользователя
    def get_fullname(self):
        return f'{self.last_name} {self.name}'

    # Вывод ошибки при попытки получение пароля
    @property
    def password(self):
        #return self._password
        raise AccessDeniedException('Sorry, you can not get this attribute.')

    # Setter, чтобы поменять пароль
    @password.setter
    def password(self, passwords):
        old_pass, new_pass = passwords
        if (old_pass == self._password):
            self._password = new_pass
        else:
            raise ValueError("Sorry, password can't be changed. Please input current password correctly!")

    # Проверка пароля
    def check_password(self, password_check):
        return bcrypt.checkpw(password_check.encode(), self._password)

    @staticmethod
    def hashed_pass(password):
        hash = bcrypt.hashpw(password=password.encode('utf-8'), salt=bcrypt.gensalt())
        return hash


# TESTING
user_1 = User('prodota25', 'Lam', 'Pham Tung', [{'country': 'Ukraine', 'city': 'Kharkive', 'index': 11618}],
                 ['11111111', '22222222'])


print(user_1.check_password('prodota125'))