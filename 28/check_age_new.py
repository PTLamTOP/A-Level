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
class InvalidDate(Exception):
    pass


# создаем класс Man
class Man:
    # принимаем имя и дату рождения при нициализации
    def __init__(self, name: str, date: str, *args, **kwargs):
        self.name = name
        self._date = self._validate_date(date=date)

    # МЕТОДЫ ДЛЯ РАБОТЫ С ДАТОЙ
    # создаем staticmethod для перевода строки в нужный формат даты ДД-ММ-ГГГГ
    @staticmethod
    def _date_formatting(date):
        return datetime.datetime.strptime(date, '%d-%m-%Y')

    # метод для проверки валидации даты
    def _validate_date(self, date):
        # форматированная дата из строки
        formatted_date = self._date_formatting(date).date()
        # сегодняшняя дата
        today_date = datetime.date.today()
        # дата дня рождения
        birthday_date = self._date_formatting(date).date()

        # проверяем date не пустая строка, если тип данных в строке
        # и проверяем если формат даты в строки является таким ДД-ММ-ГГГГ
        # проверяем если дата рождения не больше сегодняшней даты
        if date and isinstance(date, str) and formatted_date and today_date >= birthday_date:
            return formatted_date
        # вызываем кастомную ошибку, если формат не сходится
        raise InvalidDate('Invalid Date!')

    # создаем свойства через property для подсчета и вывода возраста
    @property
    def get_age(self):
        today = datetime.date.today()
        # сравниваем если текущий день и месяць, с днем и месяцям рождения. Если меньше, то возращает 0(false), в противном случае 1(true)
        age = today.year - self._date.year - ((today.month, today.day) < (self._date.month, self._date.day))
        return f'{self.name} is {age} years old'

    # создаем свойство для получения даты рождения
    @property
    def get_birthday_date(self):
        return self._date

    # создаем свойство для подсчета високосных лет
    @property
    def get_leap_year(self):
        birthday_year = self._date.year
        current_year = datetime.datetime.today().year
        leap_year = 0

        for year in range(birthday_year, current_year):
            if (year % 100 == 0) and (year % 400 == 0) or (year % 4 == 0):
                leap_year += 1
        return f'{self.name}\'ve lived for {leap_year} leap years.'


# Тест
man_1 = Man('Akira', '02-12-2000')
print(man_1.get_leap_year)