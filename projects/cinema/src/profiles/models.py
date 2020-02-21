from django.db import models
from django.conf import settings

from tickets.models import Ticket


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    def buy_tickets(self, quantity, session_obj):
        # update profile.total_cost
        self.total_cost += (quantity * session_obj.price)
        self.save()
        # update session.available_seats
        session_obj.available_seats -= quantity
        session_obj.update()
        # create ticket objects
        for q in range(quantity):
            ticket = Ticket(buyer=self.user, session=session_obj)
            ticket.save()


