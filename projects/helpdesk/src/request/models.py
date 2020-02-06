from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify


class Request(models.Model):
    LOW = 'C'
    MEDIUM = 'B'
    HIGH = 'A'
    IMPORTANCE_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )
    INPROGRESS = 'IP'
    REFUSED = 'RF'
    REREQUEST = 'RR'
    DECLINED = 'DC'
    APPROVED = 'AP'
    STATUS_CHOICES = (
        (INPROGRESS, 'In progress'),
        (REFUSED, 'Refused'),
        (REREQUEST, 'Repeated request'),
        (DECLINED, 'Declined'),
        (APPROVED, 'Approved'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='requests')
    subject = models.CharField(max_length=100, db_index=True)
    text = models.TextField()
    importance = models.CharField(max_length=2,
                                  choices=IMPORTANCE_CHOICES,
                                  default=MEDIUM)
    status = models.CharField(max_length=2,
                              choices=STATUS_CHOICES,
                              default=INPROGRESS)
    slug = models.SlugField(max_length=250, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('importance', 'created')
        index_together = (('id', 'slug'), )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.subject)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('requests:request-detail',
                       kwargs={'pk': self.pk, 'slug': self.slug})

    def __str__(self):
        return self.subject


class Comment(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='comments')

    def __str__(self):
        return f'Comment {self.body} by {self.user.username}'


class Refusal(models.Model):
    request = models.OneToOneField(Request, on_delete=models.CASCADE,
                                   related_name='refusal')
    comment = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.request.subject


class Approval(models.Model):
    request = models.OneToOneField(Request, on_delete=models.CASCADE,
                                   related_name='approval')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.request.subject


class Denial(models.Model):
    request = models.OneToOneField(Request, on_delete=models.CASCADE,
                                   related_name='denial')
    comment = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.request.subject