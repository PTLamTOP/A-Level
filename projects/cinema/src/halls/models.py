from django.db import models


class Hall(models.Model):
    name = models.CharField(max_length=100)
    seats = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Hall '{self.name}'"

    def can_be_update(self):
        hall_sessions = self.sessions.all()
        return all(not s.tickets.all() for s in hall_sessions)