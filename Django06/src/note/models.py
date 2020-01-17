from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext as _


class Author(AbstractUser):
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('author')


class Note(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='articles')
    text = models.TextField(max_length=10000, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_shared = models.BooleanField(default=False)

    def __str__(self):
        return "Author - {}, id - {}, created - {}".format(self.author.username, self.id, self.created_at)

    # def get_absolute_url(self):
    #     return reverse('note-detail', kwargs={'pk': self.id})
