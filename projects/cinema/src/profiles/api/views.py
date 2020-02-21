from rest_auth.views import LoginView, LogoutView
from rest_auth.registration.views import RegisterView

from rest_framework.permissions import IsAuthenticated
from .permissions import IsNotAuthenticated


class CustomLoginView(LoginView):
    permission_classes = (IsNotAuthenticated,)


class CustomLogoutView(LogoutView):
    permission_classes = (IsAuthenticated,)


class CustomRegisterView(RegisterView):
    permission_classes = (IsNotAuthenticated,)