from django.forms import ModelForm
from .models import EventSeating


class SeatReserveForm(ModelForm):
    class Meta:
        model = EventSeating
        fields = ['seat_location_1', 'seat_location_2', 'user_limit_reached']
