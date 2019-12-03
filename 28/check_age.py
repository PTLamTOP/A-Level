"""
1) класс, который принимает дату рождения в текстовый формат (01-05-1991).
2) написать property, которая возвращает возраст
3) вынести в статик метод метод перевода строки в дату
4) написать свойство которое говорить сколько человек прожил високосных год.
)Узнать какие годы были высокосные и потом посчитать количество)
"""

# импортируем модуль datetime для работы с датой и временем
import datetime


# создаем свой класс ошибки для обработки неправильного форматат даты
class WrongFormatDate(Exception):
    pass

class InvalidDate(Exception):
    pass


# создаем класс Man
class Man:
    _name = 'Lam'
    # принимаем имя и дату рождения при нициализации
    def __init__(self, name: str, date: str, *args , **kwargs):
        self.name = name
        self._date = self._validate_date(date=date)

    # метод для проверки валидации даты
    def _validate_date(self, date):
        today = datetime.date.today()
        if isinstance(date, str): # проверяем если тип данных в строке
            try:
                self.date_formatting(date) # проверяем если формат даты ДД-ММ-ГГГГ через метод strptime, который преобразует строку в дату по заднному формату
            except ValueError:
                raise FormatDateError('Incorrect date format, should be DD-MM-YYYY. Or incorrect date.') # вызываем кастомную ошибку, если формат не сходится
            else:
                birthday_date = self.date_formatting(date).date() # В конце добавляе date(), чтобы сошелся формат с today для сравнение.
                if today > birthday_date: # проверяем если дата рождения не больше сегодняшней даты.
                    return self.date_formatting(date).date() # возвращаем дату, если проверка формата прошла
                raise InvalidDate('Birthday date more than current date!')

    # создаем свойства через property для подсчета возраста
    @property
    def age(self):
        today = datetime.date.today()
        age = today.year - self._date.year - ((today.month, today.day) < (self._date.month, self._date.day)) # сравниваем если текущий день и месяць, с днем и месяцям рождения. Если меньше, то возращает 0(false), в противном случае 1(true)
        return f'{self.name} is {age} years old'

    # создаем свойство для получения даты рождения
    @property
    def date(self):
        return self._date

    # создаем staticmethod для перевода строки в нужный формат даты
    @staticmethod
    def date_formatting(date):
        return datetime.datetime.strptime(date, '%d-%m-%Y')

    @property
    def name(self):
        return _name

    """
    @property
    def leap_year(self):
        birthday_year = self._date.year
        today_day = datetime.today().year
        leap_year = 0
        for year in range(birthday_year, today_day):
            if (year % 100 == 0) and (year % 400 == 0):
                leap_year += 1
            elif (year % 4 == 0):
                leap_year += 1
        return f'{self.name}\'ve lived for {leap_year} leap years.'
    """


man_1 = Man('Akira', '04-12-1999')
print(man_1.get_attribute())







