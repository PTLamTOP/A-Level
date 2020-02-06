from django.shortcuts import redirect


class LoginRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated or request.get_full_path().endswith("login/") or request.get_full_path().endswith("signup/"):
            response = self.get_response(request)
            return response
        return redirect('account_login')