from django.shortcuts import render
from random import randint, choice
from string import ascii_letters, digits


def str_generator(chars=ascii_letters + digits):
    # random string generator
    size = randint(5, 13)
    return ''.join(choice(chars) for _ in range(size))


def index(request, number=None, string=''):
    # for main page 'index.html'
    url_str = request.get_full_path()
    return render(request, 'index.html', {'random_int': randint(100, 10001), 'random_str': str_generator(), 'path': url_str})


def string_button(request, string=''):
    # for page with random string 'string.html'
    url_str = request.get_full_path()
    return render(request, 'string.html', {'random_int': randint(100, 10001), 'random_str': str_generator(),
                                           'string': string, 'path': url_str})


def integer_button(request, number=None):
    # for page with random number 'integer.html'
    url_str = request.get_full_path()
    return render(request, 'integer.html', {'random_int': randint(100, 10001), 'random_str': str_generator(),
                                            'number': number, 'path': url_str})

