from django.shortcuts import redirect
from django.contrib import messages


class LoginRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            return response
        messages.add_message(request, messages.INFO, 'You are not authorized!')
        if request.get_full_path().endswith("login/") or request.get_full_path().endswith("signup/"):
            response = self.get_response(request)
            return response
        return redirect('account_login')