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
import bcrypt


class AccessDeniedException(Exception):
    pass


class InvalidDataProvided(Exception):
    pass


class User:
    def __init__(
            self, password: str, first_name: str, last_name: str,
            addresses: list, phones: list, *args, **kwargs
    ):
        self.__password = self._hash_password(password=password)
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = self._validate_addresses(addresses=addresses)
        self.phones = self._validate_phones(phones=phones)

    def _set_password(self, password):
        self.__password = self._hash_password(password=password)

    def _get_password(self):
        raise AccessDeniedException("You can't access to password")

    def _hash_password(self, password):
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return hashed

    def check_password(self, raw_password):
        return bcrypt.checkpw(raw_password.encode(), self.__password)

    password = property(_get_password, _set_password, None)

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def _validate_addresses(self, addresses):
        if addresses and isinstance(addresses, list):
            return [
                self._validate_address(address) for address in addresses
            ]
        raise InvalidDataProvided("Provide valid data")

    def _validate_address(self, address):
        required_keys = ["city", "billing_address", "country", "index"]
        if all(required_key in address for required_key in required_keys):
            return address
        raise InvalidDataProvided("Provide valid addresses")

    def _validate_phones(self, phones):
        if isinstance(phones, list) and len(phones) < 4 and all(
                (self._validate_phone(phone) for phone in phones)
        ):
            return phones
        raise InvalidDataProvided("Provide valid phones")

    def _validate_phone(self, phone):
        if isinstance(phone, str) and len(phone) <= 15:
            return phone
        raise InvalidDataProvided("Provide valid phone")


phones = ["1234567890", "0987665412", "213331313"]
invalid_phones = ["213132", "4342343", "324224224", "434222432"]
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

user = User(
    password="12345678", first_name="Kostiantyn", last_name="Salnykov",
    addresses=addresses, phones=phones
)
# user = User(
#     password="12345678", first_name="Kostiantyn", last_name="Salnykov",
#     addresses=invalid_addresses, phones=invalid_phones
# )
# user = User(
#     password="1234567", first_name="Test", last_name="Test",
#     addresses=addresses, phones=invalid_phones
# )

print(user.first_name)
print(user.last_name)
print(user.get_fullname())
print(user.check_password("12345678"))  # check valid password
print(user.check_password("123456789"))  # check invalid password
new_password = "12345"
user.password = new_password  # _set_password
# c = user.password
print(
    f"user.check_password({new_password}) =>",
    user.check_password(new_password)
)
