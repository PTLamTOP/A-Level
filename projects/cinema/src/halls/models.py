from django.db import models

from halls.api.exceptions import NotAllowedToUpdate


class Hall(models.Model):
    name = models.CharField(max_length=100)
    seats = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Hall '{self.name}'"

    def can_be_update(self):
        """
        The hall can not be updated, as a ticket was already purchased for a hall's session!
        """
        hall_sessions = self.sessions.all()
        if not all(not s.tickets.all() for s in hall_sessions):
            raise NotAllowedToUpdate