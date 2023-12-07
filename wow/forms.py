from django import forms
from .models import Customer, Vehicle, RentalService
from .constants import STATES


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vin', 'model', 'make', 'year', 'lp_state', 'lp_number']


class RentalServiceForm(forms.ModelForm):
    pickup_state = forms.ChoiceField(choices=STATES)
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all(), label='Vehicle')
    cust = forms.ModelChoiceField(queryset=Customer.objects.all(), label='Customer')

    def __init__(self, *args, **kwargs):
        super(RentalServiceForm, self).__init__(*args, **kwargs)
        self.fields['vehicle'].label_from_instance = self.get_vehicle_label
        self.fields['cust'].label_from_instance = self.get_cust_label

    def get_vehicle_label(self, obj):
        return f"{obj.make} {obj.model} {obj.year}"

    def get_cust_label(self, obj):
        if obj.cust_type == 'I':
            return f"{obj.indivcust.fname} {obj.indivcust.lname}"
        elif obj.cust_type == 'C':
            return obj.corpcust.company_name
        return ''

    class Meta:
        model = RentalService
        exclude = ['service_id']


class RentalServiceUpdateForm(forms.ModelForm):
    class Meta:
        model = RentalService
        fields = ['pickup_date', 'pickup_street', 'pickup_state', 'dropoff_date',
                  'start_odometer', 'end_odometer'
                  ]


class VehicleCreationForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
