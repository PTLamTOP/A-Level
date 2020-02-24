from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User
from filmsessions.models import Film, FilmSession
from halls.models import Hall
from tickets.models import Ticket

from datetime import timedelta, date, datetime
import pytz


class HallLoginRequiredTestCase(TestCase):
    """
    Check that user will be redirect to login page if user is not authorized.
    TEST IS PASSED!!!
    """
    def setUp(self) -> None:
        self.client = Client()
        self.hall = Hall.objects.create(name='Hall 1',
                                        seats=20)

    def test_hall_list_login_required(self):
        response = self.client.get('http://127.0.0.1:8000/halls/')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/accounts/login/?next=/halls/')

    def test_hall_create_login_required(self):
        response = self.client.get('http://127.0.0.1:8000/halls/create/')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/accounts/login/?next=/halls/create/')

    def test_hall_update_login_required(self):
        response = self.client.get('http://127.0.0.1:8000/halls/1/update/')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/accounts/login/?next=/halls/1/update/')


class HallIsAdminRequiredTestCase(TestCase):
    """
    Check that only super user has access to halls' pages.
    TEST IS PASSED!!!
    """
    def setUp(self) -> None:
        self.user = User.objects.create(username='test', is_superuser=False)
        self.user.set_password('password123')
        self.user.save()
        self.client = Client()
        self.client.post('http://127.0.0.1:8000/accounts/login/', dict(
            login='test',
            password='password123',
        ))

    def test_hall_list_is_admin_required_correct(self):
        response = self.client.get('http://127.0.0.1:8000/halls/')
        self.assertEquals(response.status_code, 403)

    def test_hall_create_is_admin_required_correct(self):
        response = self.client.get('http://127.0.0.1:8000/halls/create/')
        self.assertEquals(response.status_code, 403)

    def test_hall_update_is_admin_required_correct(self):
        response = self.client.get('http://127.0.0.1:8000/halls/1/update/')
        self.assertEquals(response.status_code, 403)


class HallCRUDTestCase(TestCase):
    """
    Check how admin will get access to halls' pages.
    """
    def setUp(self) -> None:
        # create super user
        self.admin = User.objects.create_superuser(username='test',
                                                   password='password123',
                                                   email='test@gmail.com')
        self.buyer = User.objects.create(username='buyer')
        self.client = Client()
        self.client.post('http://127.0.0.1:8000/accounts/login/', dict(
            login='test',
            password='password123',
        ))
        timezone_ = pytz.timezone("Europe/Kiev")
        local_datetime_now = timezone_.localize(datetime.now())
        self.hall = Hall.objects.create(name='Hall 1',
                                        seats=20)
        self.film = Film.objects.create(title='Film 1',
                                        genre='HR',
                                        release_year=date.today() - timedelta(days=20),
                                        period_from=date.today(),
                                        period_to=date.today() + timedelta(days=10))
        self.session_ = FilmSession.objects.create(film=self.film,
                                                   hall=self.hall,
                                                   price=50.00,
                                                   time_from=local_datetime_now,
                                                   time_to=local_datetime_now + timedelta(hours=2))

    def test_hall_list(self):
        """
        TEST IS PASSED!
        """
        response = self.client.get('http://127.0.0.1:8000/halls/')
        self.assertEquals(response.status_code, 200)

    def test_hall_create(self):
        """
        TEST IS PASSED!
        """
        response = self.client.post('http://127.0.0.1:8000/halls/create/', dict(
            name='Hall 2',
            seats=100))
        # The second hall should be created (2 halls in DB) and user should be redirected to /halls/ page
        self.assertEquals(Hall.objects.count(), 2)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/halls/')

    def test_hall_update_ok(self):
        """
        The hall can be updated as there is not any ticket to the hall.
        TEST IS PASSED!
        """
        updated_name = 'Hall 1 updated'
        response = self.client.post('http://127.0.0.1:8000/halls/1/update/', dict(
            name=updated_name,
            seats=50))
        # The first hall should be updated and user should be redirected to /halls/ page
        self.assertEquals(Hall.objects.get(id=1).name, updated_name)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/halls/')

    def test_hall_update_error(self):
        """
        The hall can not be updated as there is a ticket to the hall.
        TEST IS NOT PASSED!
        Errors:
            1) During handling of the above exception, another exception occurred:
            TypeError: argument of type 'NoneType' is not iterable
        """
        updated_name = 'Hall 1 updated'
        # create the ticket to the hall with id 1
        Ticket.objects.create(buyer=self.buyer, session=self.session_)
        # try to update the hall with new hall's name
        response = self.client.post('http://127.0.0.1:8000/halls/1/update/', dict(
            name=updated_name,
            seats=50))
        # refresh hall's data from DB
        self.hall.refresh_from_db()
        # The first hall should not be updated and admin should get a warning message
        self.assertNotEquals(Hall.objects.get(id=1).name, updated_name)
        # self.assertEquals(response.status_code, 302)
        # self.assertIn("The hall can not be updated, as a ticket was already purchased for a hall's session!",
        #               response.content.decode('utf-8'))














