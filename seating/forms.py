from django.forms import ModelForm
from .models import EventSeating


class SeatReserveForm(ModelForm):
    class Meta:
        model = EventSeating
        fields = ['event', 'seat_location', 'reserved_by']
