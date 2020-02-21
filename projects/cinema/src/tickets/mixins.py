from django.contrib.auth.mixins import UserPassesTestMixin


class NotAdminTestMixin(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_superuser
