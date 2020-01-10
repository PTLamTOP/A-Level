from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext as _
from datetime import timedelta

GENRE_CHOICES = (
    (1, _("Not selected")),
    (2, _("Comedy")),
    (3, _("Action")),
    (4, _("Beauty")),
    (5, _("Other"))
)


class Author(models.Model):
    pseudonym = models.CharField(max_length=120, blank=True, null=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='articles')
    text = models.TextField(max_length=10000, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    genre = models.IntegerField(choices=GENRE_CHOICES, default=1)

    def save(self, *args, **kwargs):
        self.created_at = timezone.now() - timedelta(years=1)
        super().save(*args, **kwargs)

    def __str__(self):
        return "Author - {}, genre - {}, id - {}, created - {}".format(self.author.name, self.genre, self.id, self.created_at)


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment = models.ForeignKey('myapp.Comment', null=True, blank=True, on_delete=models.DO_NOTHING,
                                related_name='comments')
    user = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return "{} by {}".format(self.text, self.user.name)





class Like(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='likes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return "By user {} to article {}".format(self.user.name, self.article.id)