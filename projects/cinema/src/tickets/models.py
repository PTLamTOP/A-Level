from django.db import models
from django.conf import settings

from filmsessions.models import FilmSession


class Ticket(models.Model):
    session = models.ForeignKey(FilmSession,
                                related_name='tickets',
                                on_delete=models.CASCADE)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='tickets',
                              on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket of film '{self.session.film.title}' at {self.session.time_from}"