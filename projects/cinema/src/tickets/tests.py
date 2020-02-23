from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User
from filmsessions.models import Film, FilmSession
from halls.models import Hall
from .models import Ticket

from datetime import timedelta, date, datetime
import pytz


class TicketLoginRequiredTestCase(TestCase):
    """
    Check that user will be redirect to login page if user is not authorized.
    TEST IS PASSED!!!
    """
    def setUp(self) -> None:
        self.client = Client()

    def test_ticket_create_login_required(self):
        # user is not authorized to ticket create page
        response = self.client.get('http://127.0.0.1:8000/tickets/create/')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/accounts/login/?next=/tickets/create/')

    def test_ticket_list_login_required(self):
        # user is not authorized to ticket list page
        response = self.client.get('http://127.0.0.1:8000/tickets/')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/accounts/login/?next=/tickets/')


class TicketCreateTestCase(TestCase):
    """
    Check ticket's creation: when there are enough seats, and when not enough seats.
    TEST IS PASSED!!!
    """
    def setUp(self) -> None:
        # create a standard user
        self.user = User.objects.create(username='test', is_superuser=False)
        self.user.set_password('password123')
        self.user.save()
        self.client = Client()
        self.client.post('http://127.0.0.1:8000/accounts/login/', dict(
            login='test',
            password='password123',
        ))
        timezone_ = pytz.timezone("Europe/Kiev")
        local_datetime_now = timezone_.localize(datetime.now())
        self.film = Film.objects.create(title='Film 1',
                                        genre='HR',
                                        release_year=date.today() - timedelta(days=20),
                                        period_from=date.today(),
                                        period_to=date.today() + timedelta(days=10))
        self.hall = Hall.objects.create(name='Hall 1',
                                        seats=20)
        self.session_ = FilmSession.objects.create(film=self.film,
                                                   hall=self.hall,
                                                   price=50.00,
                                                   time_from=local_datetime_now,
                                                   time_to=local_datetime_now + timedelta(hours=2))

    def test_ticket_create_enough_seats(self):
        quantity = 5
        response = self.client.post('http://127.0.0.1:8000/tickets/create/', dict(
            quantity=quantity,
            session_id=self.session_.id))

        # refresh data from DB
        self.session_.refresh_from_db()
        self.user.profile.refresh_from_db()

        # if ok -> redirect to home page
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/')

        # Tickets should be created
        self.assertEquals(Ticket.objects.count(), quantity)
        # Profile.total_cost should be increased
        self.assertEquals(self.user.profile.total_cost,
                          self.session_.price*quantity)
        # Session.available_seats should be decreased
        self.assertEquals(self.session_.available_seats,
                          self.hall.seats-quantity)

    def test_ticket_create_not_enough_seats(self):
        quantity = 100
        response = self.client.post('http://127.0.0.1:8000/tickets/create/', dict(
            quantity=quantity,
            session_id=self.session_.id))

        # refresh data from DB
        self.session_.refresh_from_db()
        self.user.profile.refresh_from_db()

        # if not ok -> redirect to home page
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/')
        # Tickets should not be created
        self.assertEquals(Ticket.objects.count(), 0)




