from django import forms
from .models import Vehicle, RentalService


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vin', 'model', 'make', 'year', 'lp_state', 'lp_number']


class RentalServiceForm(forms.ModelForm):
    class Meta:
        model = RentalService
        fields = '__all__'