from django.contrib import admin
from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'session', 'created_on')


admin.site.register(Ticket, TicketAdmin)