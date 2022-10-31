from django.contrib import admin
from .models import VenueSeat, EventSeating


@admin.register(VenueSeat)
class VenueSeatAdmin(admin.ModelAdmin):
    list_display = ('id', 'seat_location', 'is_active')


@admin.register(EventSeating)
class EventSeatingAdmin(admin.ModelAdmin):
    list_display = ('event', 'seat_location_1', 'seat_location_2',
                    'reserved_by', 'reserved_on')
    search_fields = ('event', 'reserved_by')
    list_filter = ('event', 'reserved_by')
