from django.shortcuts import redirect
from django.contrib import messages
from datetime import datetime, timedelta
import pytz

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated or request.get_full_path().endswith("login/"):
            response = self.get_response(request)
            return response

        return redirect('login')


class CheckConfirmedEmail:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            if request.user.email_confirmed == False:
                messages.add_message(request, messages.INFO, 'Please confirm your email to get 20% of discount!!!')
        except AttributeError:
            if request.user.is_anonymous and not request.get_full_path().endswith("login/"):
                return redirect('login')

        response = self.get_response(request)
        return response


class CheckEmailExpirationDate:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        current_date = datetime.now(tz=pytz.UTC)
        three_days = timedelta(days=3)
        try:
            if (request.user.email_confirmed == False) and (current_date - request.user.date_joined) > three_days:
                request.user.is_active = False
                request.user.save()
        except AttributeError:
            if request.user.is_anonymous and not request.get_full_path().endswith("login/"):
                return redirect('login')

        response = self.get_response(request)
        return response


