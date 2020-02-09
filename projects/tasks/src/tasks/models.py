from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify


class Card(models.Model):
    NEW = 'NW'
    INPROGRESS = 'IP'
    INQA = 'IQ'
    READY = 'RD'
    DONE = 'DN'
    STATUS_CHOICES = (
        (NEW, 'New'),
        (INPROGRESS, 'In progress'),
        (INQA, 'In QA'),
        (READY, 'Ready'),
        (DONE, 'Done'),
    )
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='created_tasks')
    executor = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='tasks',
                                 blank=True,
                                 null=True)
    text = models.TextField()
    status = models.CharField(max_length=2,
                              choices=STATUS_CHOICES,
                              default=NEW)
    slug = models.SlugField(max_length=250, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        index_together = (('id', 'slug'), )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"task#{self.id}-{self.status}-by_{self.creator}-on_{self.executor}")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tasks:card-detail',
                       kwargs={'pk': self.pk, 'slug': self.slug})

    def __str__(self):
        return f"task#{self.id}-{self.status}-by_{self.creator}-on_{self.executor}"