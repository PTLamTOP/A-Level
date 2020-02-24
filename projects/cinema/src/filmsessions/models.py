from django.db import models
from django.conf import settings

from django.urls import reverse

from django_fields import DefaultStaticImageField

from halls.models import Hall

from django.contrib import messages

from filmsessions.api.exceptions import InvalidSessionTime, NotAvailableTime, NotAllowedToUpdate


class Film(models.Model):
    ACTION = 'AC'
    ADVENTURE = 'AD'
    COMEDY = 'CM'
    CRIME = 'CR'
    DRAMA = 'DR'
    HISTORICAL = 'HS'
    HORROR ='HR'
    MUSICALS = 'MC'
    SCIENCE = 'SC'
    WAR = 'WR'
    WESTERNS = 'WN'
    GENRES_CHOICES = (
        (ACTION, 'Action'),
        (ADVENTURE, 'Adventure'),
        (COMEDY, 'Comedy'),
        (CRIME, 'Crime'),
        (DRAMA, 'Drama'),
        (HISTORICAL, 'Historical'),
        (HORROR, 'Horror'),
        (MUSICALS, 'Musicals'),
        (SCIENCE, 'Science'),
        (WAR, 'War'),
        (WESTERNS, 'Westerns'),
    )
    title = models.CharField(max_length=200)
    picture = DefaultStaticImageField(upload_to='pictures/%Y/%m/%d',
                                      blank=True,
                                      default_image_path=settings.DEFAULT_IMAGE_PATH)
    genre = models.CharField(choices=GENRES_CHOICES, max_length=2)
    description = models.TextField()
    release_year = models.DateField()
    period_from = models.DateField()
    period_to = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Film '{self.title}'"


class FilmSession(models.Model):
    film = models.ForeignKey(Film,
                             related_name='sessions',
                             on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall,
                             related_name='sessions',
                             on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    time_from = models.DateTimeField()
    time_to = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    available_seats = models.PositiveIntegerField(blank=True)

    def save(self, *args, **kwargs):
        """
        Set initial available seats in session as amount of seats in a hall.
        """
        if not self.available_seats:
            self.available_seats = self.hall.seats
        super().save(*args, **kwargs)

    def update(self, *args, **kwargs):
        """
        It is a default safe method.
        """
        super().save(*args, **kwargs)

    def update_seats_amount(self, new_amount, *args, **kwargs):
        """
        Method to update sessions's available seats.
        """
        self.available_seats = new_amount
        super().save(*args, **kwargs)

    def has_enough_seats(self, quantity, request):
        """
        Method for checking if the session has enough seats for buying tickets.
        """
        if self.available_seats == 0:
            messages.add_message(request, messages.INFO, f'Sorry, there is not any ticket.')
            return False
        elif self.available_seats >= quantity:
            ticket_end = 's' if quantity > 1 else ''
            messages.add_message(request, messages.SUCCESS, f"You have bought {quantity} ticket{ticket_end}.")
            return True
        messages.add_message(request, messages.INFO, f'Sorry, there are only {self.available_seats} tickets.')

    def check_time_with_session_time(self, request, time_from, time_to):
        """
        :param time_from: start time of a new session
        :param time_to: end time of a new session
        :return: True if test was passed

        Test:
            1) (time_from < self.time_from and time_to < self.time_from) - ___new___|session_time|___ new session
            should be before existing session.
                OR
            2) (time_from > self.time_to and time_to > self.time_to) - ____|session_time|___new___ new session should
            be after existing session.
        """
        if (time_from < self.time_from and time_to < self.time_from) \
                or (time_from > self.time_to and time_to > self.time_to):
            return True
        raise NotAvailableTime

    @staticmethod
    def check_valid_sessiontime(request, time_from, time_to, film):
        """
        :param time_from: start time of a new session
        :param time_to: end time of a new session
        :param film: film object which will be in a new session
        :return: True if test was passed

        Test:
            1) (time_to > time_from) - end time should be more than start time;
            2) (time_from.date() >= film.period_from and time_to.date() <= film.period_to) - session
            date should be in between film's screening time.
        """
        if time_to > time_from:
            if time_from.date() >= film.period_from \
                    and time_to.date() <= film.period_to:
                return True
        raise InvalidSessionTime

    @classmethod
    def create_session_validation(cls, request, time_from,
                                  time_to, film_obj, all_hall_sessions):
        """
        Use methods: check_valid_sessiontime and check_time_with_session_time in one method.
        """
        if cls.check_valid_sessiontime(request=request, time_from=time_from,
                                       time_to=time_to, film=film_obj):
            if all(s.check_time_with_session_time(request=request,
                                                  time_from=time_from,
                                                  time_to=time_to) for s in all_hall_sessions):
                return True

    def update_validate(self):
        """
        The session can be updated if session does not have any ticket.
        """
        if not self.tickets.all():
            return True
        raise NotAllowedToUpdate

    def __str__(self):
        return f"Session of film '{self.film.title}' at {self.time_from}"

    def get_absolute_url(self):
        return reverse('film-sessions:session-update', kwargs={'pk': self.pk})

