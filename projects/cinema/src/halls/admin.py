from django.contrib import admin
from .models import Hall


class HallAdmin(admin.ModelAdmin):
    list_display = ('name', 'seats', )


admin.site.register(Hall, HallAdmin)
