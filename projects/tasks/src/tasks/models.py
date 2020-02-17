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

    def notadmin_card_status_change(self, request, move_index):
        valid_statuses = ['IP', 'IQ', 'RD', ]
        current_status_index = valid_statuses.index(self.status)
        try:
            if current_status_index == 0 and move_index == -1:
                self.status = 'IP'
            new_status = valid_statuses[current_status_index + move_index]
        except IndexError:
            new_status = 'RD'
        self.status = new_status
        self.save()

    def admin_card_status_change(self, request, move_index):
        valid_statuses = ['RD', 'DN', ]
        current_status_index = valid_statuses.index(self.status)
        try:
            if current_status_index == 0 and move_index == -1:
                self.status = 'RD'
            new_status = valid_statuses[current_status_index + move_index]
        except IndexError:
            new_status = 'DN'
        self.status = new_status
        self.save()

    def __str__(self):
        return f"task#{self.id}-{self.status}-by_{self.creator}-on_{self.executor}"