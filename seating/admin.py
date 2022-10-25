from django.contrib import admin
from .models import VenueSeat, EventSeating


@admin.register(VenueSeat)
class VenueSeatAdmin(admin.ModelAdmin):
    list_display = ('seat_location', 'is_active',)


@admin.register(EventSeating)
class EventSeatingAdmin(admin.ModelAdmin):
    list_display = ('event', 'seat_location', 'reserved_by', 'reserved_on',)
    search_fields = ('event', 'seat_location',)
    list_filter = ('event', 'seat_location',)
