from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from datetime import timedelta
from django.urls import reverse


SEX_CHOICES = (
        (1, _("male")),
        (2, _("female")),
    )


class Animal(models.Model):
    TYPE_CHOICE = (
        (1, _("badger")),
        (2, _("monkey")),
        (3, _("bear")),
    )

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.IntegerField(choices=SEX_CHOICES)
    type = models.IntegerField(choices=TYPE_CHOICE)
    arrived_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('zoo:animal-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-arrived_at']


class Visitor(User):
    age = models.IntegerField()
    sex = models.IntegerField(choices=SEX_CHOICES)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = _('visitor')


class Ticket(models.Model):
    age_limit = models.IntegerField(default=8)
    created_at = models.DateTimeField(default=timezone.now)
    expired_at = models.DateTimeField(default=timezone.now)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, related_name='tickets', null=False)

    def save(self, *args, **kwargs):
        self.expired_at = timezone.now() - timedelta(days=1)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ticket {self.id} for visitor: {self.visitor.username}"


class Visit(models.Model):
    """
    Анология many-to-many
    """
    # One Visitor has a lot of visits
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, related_name='visits', null=False)
    # One Visit has a lot of animals, one Animal has a lot of visits
    animals = models.ManyToManyField(Animal)
    visit_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.visitor.username} visited {self.animals}."


