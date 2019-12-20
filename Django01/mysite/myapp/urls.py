from django.urls import path, register_converter
from .converters import FourDigitYearConverter, TwoDigitThreeLetter, TestWithHyphen, PhoneNumber
from .views import special_case_2003, year_archive, nnsss, n_s_n, phone


register_converter(FourDigitYearConverter, 'yyyy')
register_converter(TwoDigitThreeLetter, 'nnsss')
register_converter(TestWithHyphen, 'n_s_n')
register_converter(PhoneNumber, 'phone')

urlpatterns = [
    path('2003/', special_case_2003),
    path('<yyyy:year>/', year_archive),
    path('<nnsss:text>/', nnsss),
    path('<n_s_n:text>', n_s_n),
    path('<phone:text>', phone),
]