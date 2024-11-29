from django import forms
from .models import Bus

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['name', 'bus_number', 'from_location', 'to_location', 'journey_time', 'ticket_price', 'no_of_seats']
