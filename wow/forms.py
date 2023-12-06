from django import forms
from .models import Vehicle, RentalService


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vin', 'model', 'make', 'year', 'lp_state', 'lp_number']


class RentalServiceForm(forms.ModelForm):
    class Meta:
        model = RentalService
        fields = ['pickup_date', 'pickup_street', 'pickup_state', 'dropoff_date',
                  'start_odometer', 'end_odometer'
                  ]