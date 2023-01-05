from django.contrib import admin
from .models import VenueSeat, EventSeating


@admin.register(VenueSeat)
class VenueSeatAdmin(admin.ModelAdmin):
    """
    Particularizes the layout and content of the admin interface
    for the VenueSeat model
    """
    list_display = ('id', 'seat_location', 'is_active')


@admin.register(EventSeating)
class EventSeatingAdmin(admin.ModelAdmin):
    """
    Particularizes the layout and content of the admin interface
    for the EventSeating model
    """
    list_display = ('event', 'seat_location_1', 'seat_location_2',
                    'reserved_by', 'reserved_on', 'user_limit_reached')
    search_fields = ('event', 'reserved_by')
    list_filter = ('event', 'reserved_by')
    actions = ['limit_reached', 'can_book_seats']

    def limit_reached(self, request, queryset):
        queryset.update(user_limit_reached=True)

    def can_book_seats(self, request, queryset):
        queryset.update(user_limit_reached=False)
