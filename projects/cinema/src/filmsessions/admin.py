from django.contrib import admin
from .models import Hall, FilmSession, Film, Ticket


class FilmSessionAdmin(admin.ModelAdmin):
    list_display = ('hall', 'film', 'time_from', 'time_to', 'available_seats', 'get_all_seats', )

    def get_all_seats(self, obj):
        return obj.hall.seats
    get_all_seats.admin_order_field = 'all seats'
    get_all_seats.short_description = 'All seats in hall'


class TicketAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'session', 'created_on')


admin.site.register(Hall)
admin.site.register(FilmSession, FilmSessionAdmin)
admin.site.register(Film)
admin.site.register(Ticket, TicketAdmin)
