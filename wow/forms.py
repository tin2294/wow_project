from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Vehicle, RentalService
from .constants import STATES
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Customer

class AccountRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]


class CustomerProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "address_houseno",
            "address_street",
            "address_state",
            "address_city",
            "address_zipcode",
            "phone",
            "cust_type"
        ]


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
    classid = forms.ModelChoiceField(queryset=Vclass.objects.all(), label='Type of Vehicle')
    office = forms.ModelChoiceField(queryset=Office.objects.all(), label='Office')

    def __init__(self, *args, **kwargs):
        super(VehicleCreationForm, self).__init__(*args, **kwargs)
        self.fields['classid'].label_from_instance = self.get_class
        self.fields['office'].label_from_instance = self.get_office

    def get_class(self, obj):
        return f"{obj.class_name}, ${obj.daily_rate}"

    def get_office(self, obj):
        return f"{obj.address_houseno} {obj.address_street}, {obj.address_city}, {obj.address_zipcode}, {obj.address_state}"

    class Meta:
        model = Vehicle
        exclude = ['vehicle_id']

