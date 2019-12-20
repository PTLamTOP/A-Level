from django.shortcuts import render
from random import randint, choice
from string import ascii_letters, digits



def str_generator(chars=ascii_letters + digits):
    # random string generator
    size = randint(5, 13)
    return ''.join(choice(chars) for _ in range(size))


# Create your views here.
def index(request, number=None, string=''):
    if number:
        # for page with random number 'integer.html'
        return render(request, 'integer.html', {'random_int': randint(100, 10001), 'random_str': str_generator(),
                                                'number': number})
    elif string:
        # for page with random string 'string.html'
        return render(request, 'string.html', {'random_int': randint(100, 10001), 'random_str': str_generator(),
                                               'string_len': len(string)})
    # for main page 'index.html'
    return render(request, 'index.html', {'random_int': randint(100, 10001), 'random_str': str_generator()})
