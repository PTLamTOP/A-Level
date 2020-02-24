from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User
from filmsessions.models import Film, FilmSession
from halls.models import Hall
from tickets.models import Ticket

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
        # create super user
        self.admin = User.objects.create_superuser(username='testAdmin',
                                                   password='password123',
                                                   email='test@gmail.com')
        self.buyer = User.objects.create(username='testUser')
        self.client = Client()
        # admin logged in
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

    def test_filmsession_create_ok(self):
        """
        TEST IS PASSED!!!
        """
        dt_now = datetime.now()
        time_from_str = dt_now.strftime('%Y-%m-%d %H:%M')
        time_to_str = (dt_now + timedelta(hours=2)).strftime('%Y-%m-%d %H:%M')
        response = self.client.post('http://127.0.0.1:8000/session/create/', dict(
            film=self.film.id,
            hall=self.hall.id,
            price=50.00,
            time_from=time_from_str,
            time_to=time_to_str))
        # The session should be created and admin should be redirected to home page
        self.assertEquals(FilmSession.objects.count(), 1)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/')

    def test_filmsession_update_ok(self):
        """
        TEST IS PASSED!!!
        """
        timezone_ = pytz.timezone("Europe/Kiev")
        FilmSession.objects.create(film=self.film,
                                   hall=self.hall,
                                   price=50.00,
                                   time_from=timezone_.localize(datetime.now()),
                                   time_to=timezone_.localize(datetime.now()) + timedelta(hours=2))
        response = self.client.post('http://127.0.0.1:8000/session/1/update/', dict(
            film=self.film.id,
            hall=self.hall.id,
            price=100.00,
            time_from=datetime.now(),
            time_to=datetime.now() + timedelta(hours=5)
        ))
        f_session = FilmSession.objects.get(id=1)
        f_session.refresh_from_db()
        # The session should be updated with new price and admin should be redirected to home page
        self.assertEquals(float(FilmSession.objects.get(id=1).price), 100.00)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/')

    def test_filmsession_update_wrong(self):
        """
        Check that the session can not be updated, as a ticket was already bought.
        TEST IS PASSED!!!
        """
        timezone_ = pytz.timezone("Europe/Kiev")
        FilmSession.objects.create(film=self.film,
                                   hall=self.hall,
                                   price=50.00,
                                   time_from=timezone_.localize(datetime.now()),
                                   time_to=timezone_.localize(datetime.now()) + timedelta(hours=2))
        session_ = FilmSession.objects.get(id=1)
        Ticket.objects.create(buyer=self.buyer, session=session_)
        response = self.client.post('http://127.0.0.1:8000/session/1/update/', dict(
            film=self.film.id,
            hall=self.hall.id,
            price=100.00,
            time_from=datetime.now(),
            time_to=datetime.now() + timedelta(hours=5)
        ))
        session_.refresh_from_db()
        # The session should not be updated and admin should get warning message
        self.assertEquals(float(FilmSession.objects.get(id=1).price), 50.00)
        self.assertEquals(response.status_code, 302)

    def test_filmsession_create_timeto_less_than_timefrom(self):
        """
        Check error when time_to is less than time_from.
        TEST IS PASSED!!!
        """
        dt_now = datetime.now()
        time_from_str = (dt_now + timedelta(hours=2)).strftime('%Y-%m-%d %H:%M')
        time_to_str = dt_now.strftime('%Y-%m-%d %H:%M')
        response = self.client.post('http://127.0.0.1:8000/session/create/', dict(
            film=self.film.id,
            hall=self.hall.id,
            price=50.00,
            time_from=time_from_str,
            time_to=time_to_str))
        # The session should not be created
        self.assertEquals(FilmSession.objects.count(), 0)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/session/create/')

    def test_filmsession_create_time_is_out_screening_period(self):
        """
        Check error when session's time is out of film's screening period.
        TEST IS PASSED!!!
        """
        dt_out_of_screening_time = datetime.now() + timedelta(days=60)
        time_from_str = dt_out_of_screening_time.strftime('%Y-%m-%d %H:%M')
        time_to_str = (dt_out_of_screening_time + timedelta(days=61)).strftime('%Y-%m-%d %H:%M')
        response = self.client.post('http://127.0.0.1:8000/session/create/', dict(
            film=self.film.id,
            hall=self.hall.id,
            price=50.00,
            time_from=time_from_str,
            time_to=time_to_str))
        # The session should be created and admin will get warning message
        self.assertEquals(FilmSession.objects.count(), 0)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/session/create/')

    def test_filmsession_create_not_available_time(self):
        """
        Check error when there is already a session during this time in the same hall!.
        TEST IS PASSED!!!
        """
        timezone_ = pytz.timezone("Europe/Kiev")
        FilmSession.objects.create(film=self.film,
                                   hall=self.hall,
                                   price=50.00,
                                   time_from=timezone_.localize(datetime.now()),
                                   time_to=timezone_.localize(datetime.now()) + timedelta(hours=2))
        dt_now = datetime.now()
        time_from_str = dt_now.strftime('%Y-%m-%d %H:%M')
        time_to_str = (dt_now + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M')
        response = self.client.post('http://127.0.0.1:8000/session/create/', dict(
            film=self.film.id,
            hall=self.hall.id,
            price=50.00,
            time_from=time_from_str,
            time_to=time_to_str))
        # The second session should not be created
        self.assertEquals(FilmSession.objects.count(), 1)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/session/create/')








