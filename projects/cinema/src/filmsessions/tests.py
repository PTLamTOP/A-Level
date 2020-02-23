from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User
from filmsessions.models import Film, FilmSession
from halls.models import Hall
from tickets.models import Ticket

from halls.api.exceptions import NotAllowedToUpdate

from datetime import timedelta, date, datetime
import pytz


class FilmTestCase(TestCase):
    """
    Check that user will be redirect to login page if user is not authorized to films' pages.
    Check that film is created correctly.
    TEST IS PASSED!!!
    """
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create(username='testUser', is_superuser=False)
        self.user.set_password('password123')
        self.user.save()
        # create super user
        self.admin = User.objects.create_superuser(username='testAdmin',
                                                   password='password123',
                                                   email='test@gmail.com')

    def test_hall_create_login_required(self):
        response = self.client.get('http://127.0.0.1:8000/film/create/')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/accounts/login/?next=/film/create/')

    def test_film_create_is_admin_required(self):
        self.client.post('http://127.0.0.1:8000/accounts/login/', dict(
            login='testUser',
            password='password123',
        ))
        response = self.client.get('http://127.0.0.1:8000/film/create/')
        self.assertEquals(response.status_code, 403)

    def test_film_create(self):
        # admin logged in
        self.client.post('http://127.0.0.1:8000/accounts/login/', dict(
            login='testAdmin',
            password='password123',
        ))
        # create film
        response = self.client.post('http://127.0.0.1:8000/film/create/', dict(
            title='Film 1',
            genre='HR',
            description='Some text.',
            release_year=date.today() - timedelta(days=20),
            period_from=date.today(),
            period_to=date.today() + timedelta(days=10)))
        # The film should be created in DB and admin should be redirected to home page
        self.assertEquals(Film.objects.count(), 1)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/')


class SessionCRUDTestCase(TestCase):
    """
    Check how admin will get access to sessions' pages.
    """
    def setUp(self) -> None:
        timezone_ = pytz.timezone("Europe/Kiev")
        dt_now = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M'), '%Y-%m-%d %H:%M')
        self.local_datetime_now = timezone_.localize(dt_now)
        # create super user
        self.admin = User.objects.create_superuser(username='testAdmin',
                                                   password='password123',
                                                   email='test@gmail.com')
        self.buyer = User.objects.create(username='testUser')
        self.client = Client()
        self.client.post('http://127.0.0.1:8000/accounts/login/', dict(
            login='testAdmin',
            password='password123',
        ))
        self.hall = Hall.objects.create(name='Hall 1',
                                        seats=20)
        self.film = Film.objects.create(title='Film 1',
                                        genre='HR',
                                        release_year=date.today() - timedelta(days=20),
                                        period_from=date.today(),
                                        period_to=date.today() + timedelta(days=10))

    def test_filmsessin_create_ok(self):
        # Session can not be created as ValueError: unconverted data remains: :00+02:00
        response = self.client.post('http://127.0.0.1:8000/session/create/', dict(
            film=self.film.id,
            hall=self.hall.id,
            price=50.00,
            time_from=self.local_datetime_now,
            time_to=self.local_datetime_now + timedelta(hours=2)))
        FilmSession.refresh_from_db()
        # The second hall should be created (2 halls in DB) and user should be redirected to /halls/ page
        self.assertEquals(FilmSession.objects.count(), 1)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/')




