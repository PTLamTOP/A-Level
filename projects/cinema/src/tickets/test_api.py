from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from django.contrib.auth.models import User
from filmsessions.models import Film, FilmSession
from halls.models import Hall
from .models import Ticket

from datetime import timedelta, date, datetime
import pytz


class TicketLoginRequiredTestCase(APITestCase):
    """
    Check that user will be redirect to login form if user is not authorized.
    TEST IS PASSED!!!
    """
    def setUp(self) -> None:
        self.client = APIClient()

    def test_ticket_list_login_required(self):
        response = self.client.get('/tickets/api')
        # user will be redirected to login
        self.assertEquals(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)


class TicketCreateTestCase(APITestCase):
    """
    Check ticket's creation: when there are enough seats, and when not enough seats.
    TEST IS PASSED!!!
    """
    def setUp(self) -> None:
        self.client = APIClient()
        # create a standard user
        self.user = User.objects.create(username='test',
                                        email='test@gmail.com',
                                        is_superuser=False)
        self.user.set_password('test2020')
        self.user.save()
        # login
        data = dict(username='test',
                    email='test@gmail.com',
                    password='test2020')
        self.client.post('/rest-auth/login/', data, format='json')
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
        """
        TEST IS PASSED!!!
        """
        response = self.client.post('/tickets/api/', dict(session=self.session_.id), format='json')

        # refresh data from DB
        self.session_.refresh_from_db()
        self.user.profile.refresh_from_db()

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        # Ticket should be created
        self.assertEquals(Ticket.objects.count(), 1)
        # Profile.total_cost should be increased
        self.assertEquals(self.user.profile.total_cost,
                          self.session_.price)
        # Session.available_seats should be decreased
        self.assertEquals(self.session_.available_seats,
                          self.hall.seats-1)

    def test_ticket_create_not_enough_seats(self):
        """
        TEST IS PASSED!!!
        """
        # set available seats to zero
        self.session_.available_seats = 0
        self.session_.update()
        self.session_.refresh_from_db()
        # try to buy a ticket
        response = self.client.post('/tickets/api/', dict(session=self.session_.id), format='json')

        # refresh data from DB
        self.session_.refresh_from_db()
        self.user.profile.refresh_from_db()

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("There is not any available ticket.", response.content.decode('utf-8'))

        # Ticket should not be created
        self.assertEquals(Ticket.objects.count(), 0)
        # Profile.total_cost should not be increased
        self.assertEquals(self.user.profile.total_cost, 0)
        # Session.available_seats should not be decreased
        self.assertEquals(self.session_.available_seats, 0)