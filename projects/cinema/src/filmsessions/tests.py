from django.test import TestCase
from django.contrib.auth.mixins import UserPassesTestMixin


class AdminTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

