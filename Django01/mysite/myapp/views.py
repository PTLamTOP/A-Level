from django.http import HttpResponse

# Create your views here.
def special_case_2003(request):
    return HttpResponse('It is article 2003!')


def year_archive(request, year=None):
    return HttpResponse(f'It is article in {year}!')

def nnsss(request, text=''):
    return HttpResponse(f'2 digits, 3 letter: {text}!')

def n_s_n(request, text=''):
    return HttpResponse(f'digit-letter-digit: {text}!')

def phone(request, text=''):
    return HttpResponse(f'phone: {text}!')

