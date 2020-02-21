from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User
from filmsessions.models import Film, FilmSession
from halls.models import Hall
from .models import Ticket

from datetime import timedelta, date, datetime
import pytz

# timezone_ = pytz.timezone('Europe/Kiev')
# local_datetime_now = timezone_.localize(datetime.now())
#
# clietn = Client()
# user = User.objects.create(username='testtt', password='password123')
# film = Film.objects.create(title='Film 1',
#                            genre='HR',
#                            release_year=2020,
#                            period_from=date.today(),
#                            period_to=date.today() + timedelta(days=10)
#                            )
# hall = Hall.objects.create(name='Hall 1',
#                            seats=20)
# session_ = FilmSession.objects.create(film=film,
#                                       hall=hall,
#                                       price=50.00,
#                                       time_from=local_datetime_now,
#                                       time_to=local_datetime_now + timedelta(hours=2)
#                                       )


class TicketLoginRequiredTestCase(TestCase):
    """
    Check that user will be redirect to login page if user is not authorized.
    TEST IS PASSED!!!
    """
    def setUp(self) -> None:
        self.client = Client()

    def test_ticket_create_login_required(self):
        response = self.client.get('http://127.0.0.1:8000/tickets/create/')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/accounts/login/?next=/tickets/create/')

    def test_ticket_list_login_required(self):
        response = self.client.get('http://127.0.0.1:8000/tickets/')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/accounts/login/?next=/tickets/')


class TicketCreateTestCase(TestCase):
    # QUESTION: TypeError: expected string or bytes-like object

    def setUp(self) -> None:
        self.client = Client()
        logged_in = self.client.login(username)
        client.post('http://127.0.0.1:8000/accounts/login/', dict(
            username=user.username,
            password=user.password,
        ))

    def test_ticket_create_enough_seats(self):
        quantity = 5
        response = client.post('http://127.0.0.1:8000/tickets/create/', dict(
            quantity=quantity,
            session_id=session_.id))

        # refresh data from DB
        session_.refresh_from_db()
        user.profile.refresh_from_db()

        # if ok -> redirect to home page
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/')

        # Tickets should be created
        self.assertEquals(Ticket.objects.count(), quantity)
        # Profile.total_cost should be increased
        self.assertEquals(user.profile.total_cost,
                          session_.price*quantity)
        # Session.available_seats should be decreased
        self.assertEquals(session_.available_seats,
                          session_.available_seats-quantity)

    def test_ticket_create_not_enough_seats(self):
        quantity = 100
        response = client.post('http://127.0.0.1:8000/tickets/create/', dict(
            quantity=quantity,
            session_id=session_.id))

        # refresh data from DB
        session_.refresh_from_db()
        user.profile.refresh_from_db()

        # if not ok -> redirect to home page
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/')
        self.assertIn("Sorry, there", response.content.decode('utf-8'))



