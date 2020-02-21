from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User
from filmsessions.models import Film, FilmSession
from halls.models import Hall

from datetime import timedelta, date, datetime
import pytz

# ОШИБКИ
# 1) В СОЗДАНИИ ОБЪЕКТА ПРИ ПЕРЕДАЧИ ДАТЫ И ВРЕМЯ. TypeError: expected string or bytes-like object
# 2) КЛИЕНТ не логиниться при создании пользователя через модели, НО если делать запрос пост на регистрацю, то все ОК
timezone_ = pytz.timezone('Europe/Kiev')
local_datetime_now = timezone_.localize(datetime.now())

client = Client()
film = Film.objects.create(title='Film 1',
                           genre='HR',
                           release_year=date.today(),
                           period_from=date.today(),
                           period_to=date.today() + timedelta(days=10)
                           )
hall = Hall.objects.create(name='Hall 1',
                           seats=20)
session_ = FilmSession.objects.create(film=film,
                                      hall=hall,
                                      price=50.00,
                                      time_from=local_datetime_now,
                                      time_to=local_datetime_now + timedelta(hours=2)
                                      )


class HallLoginRequiredTestCase(TestCase):
    def setUp(self) -> None:
        self.hall = Hall.objects.create(id=1,
                                        name='Hall 1',
                                        seats=20)

    def test_hall_list_login_required(self):
        response = client.get('http://127.0.0.1:8000/halls/')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/accounts/login/?next=/halls/')

    def test_hall_create_login_required(self):
        response = client.get('http://127.0.0.1:8000/halls/create/')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/accounts/login/?next=/halls/create/')

    def test_hall_update_login_required(self):
        response = client.get('http://127.0.0.1:8000/halls/1/update/')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/accounts/login/?next=/halls/1/update/')


class HallGetActionIsAdminTestCase(TestCase):
    # DOES NOT WORK!!! Do not login
    def setUp(self) -> None:
        self.admin = User.objects.create_superuser(username='AdminTest',
                                                   password='password123',
                                                   email='bla@bla.bla')
        self.client.post('http://127.0.0.1:8000/accounts/login/', dict(
            username=self.admin.username,
            password=self.admin.password,
        ))

    def test_hall_list_is_admin_required_correct(self):
        response = client.get('http://127.0.0.1:8000/halls/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.url, 'http://127.0.0.1:8000/halls/')

    def test_hall_create_is_admin_required_correct(self):
        response = client.get('http://127.0.0.1:8000/halls/create/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.url, 'http://127.0.0.1:8000/halls/create')

    def test_hall_update_is_admin_required_correct(self):
        response = client.get('http://127.0.0.1:8000/halls/1/update/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.url, 'http://127.0.0.1:8000/halls/1/update/')


class HallGetActionNotAdminTestCase(TestCase):
    # DOES NOT WORK!!! # Do not logined
    def setUp(self) -> None:
        self.is_not_admin = User.objects.create(username='UserTest', password='password123')
        self.hall = Hall.objects.create(id=1,
                                        name='Hall 1',
                                        seats=20)
        client.post('http://127.0.0.1:8000/accounts/login/', dict(
            username=self.is_not_admin.username,
            password=self.is_not_admin.password,
        ))

    def test_hall_list_is_admin_required_wrong(self):
        response = client.get('http://127.0.0.1:8000/halls/')
        self.assertEquals(response.status_code, 403)

    def test_hall_create_is_admin_required_wrong(self):
        response = client.get('http://127.0.0.1:8000/halls/create/')
        self.assertEquals(response.status_code, 403)

    def test_hall_update_is_admin_required_wrong(self):
        response = client.get('http://127.0.0.1:8000/halls/1/update/')
        self.assertEquals(response.status_code, 403)


class HallCreateTestCase(TestCase):
    # DOES NOT WORK!!! Do not login
    def setUp(self) -> None:
        self.admin = User.objects.create(username='AdminTest',
                                         password='password123',
                                         is_superuser=True)
        self.hall = Hall.objects.create(id=1,
                                        name='Hall 1',
                                        seats=20)
        client.post('http://127.0.0.1:8000/accounts/login/', dict(
            username=self.admin.username,
            password=self.admin.password,
        ))
