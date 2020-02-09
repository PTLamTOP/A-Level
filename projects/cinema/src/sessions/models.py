from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify


class Hall(models.Model):
    name = models.CharField(max_length=100)
    seats = models.PositiveIntegerField()

    def __str__(self):
        return f"Hall {self.name}"


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
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d',
                                height_field=500,
                                width_field=500)
    genre = models.CharField(choices=GENRES_CHOICES, max_length=2)
    description = models.TextField()
    release_year = models.DateField()
    period_from = models.DateField()
    period_to = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Film '{self.title}'"


class Session(models.Model):
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
    available_seats = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        """
        Initial available seats is equal to amount of seats in a hall.
        """
        if not self.available_seats:
            self.available_seats = self.hall.seats
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Session of file '{self.film.title}' at {self.time_from}"


class Ticket(models.Model):
    session = models.ForeignKey(Session,
                                related_name='tickets',
                                on_delete=models.CASCADE)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='tickets',
                              on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket of film '{self.session.film.title}' at {self.session.time_from}"