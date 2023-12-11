from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Vehicle, RentalService, VClass, Office, CorpCust, IndivCust, Payment, IndivDiscount, CorpDiscount, InvoiceIndivDiscount, InvoiceCorpDiscount
from .constants import STATES
from django.contrib.auth.models import User

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


class CorpCustCreationForm(forms.ModelForm):
    class Meta:
        model = CorpCust
        fields = [
            "company_name",
            "company_number",
            "emp_id"
        ]

class IndivCustCreationForm(forms.ModelForm):
    class Meta:
        model = IndivCust
        fields = [
            "license_no",
            "insurance_co",
            "insurance_policy_num"
        ]


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vin', 'model', 'make', 'year', 'lp_state', 'lp_number']


class RentalServiceForm(forms.ModelForm):
    pickup_state = forms.ChoiceField(choices=STATES)
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all(), label='Vehicle')
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), label='Customer')

    def __init__(self, *args, **kwargs):
        super(RentalServiceForm, self).__init__(*args, **kwargs)
        self.fields['vehicle'].label_from_instance = self.get_vehicle_label
        self.fields['customer'].label_from_instance = self.get_cust_label

    def get_vehicle_label(self, obj):
        return f"{obj.make} {obj.model} {obj.year}"

    def get_cust_label(self, obj):
        if hasattr(obj, 'indivcust') and obj.cust_type == 'I':
            return f"{obj.indivcust.customer.user.first_name} {obj.indivcust.customer.user.last_name}"
        elif hasattr(obj, 'corpcust') and obj.cust_type == 'C':
            return obj.corpcust.company_name
        return ''

    class Meta:
        model = RentalService
        exclude = ['id']


class RentalServiceCustVehInclForm(forms.ModelForm):
    pickup_state = forms.ChoiceField(choices=STATES)

    def __init__(self, *args, **kwargs):
        super(RentalServiceCustVehInclForm, self).__init__(*args, **kwargs)

    class Meta:
        model = RentalService
        exclude = ['id', 'customer', 'vehicle', 'end_odometer', 'is_active']


class RentalServiceStaffVehInclForm(forms.ModelForm):
    pickup_state = forms.ChoiceField(choices=STATES)
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), label='Customer')

    def __init__(self, *args, **kwargs):
        super(RentalServiceStaffVehInclForm, self).__init__(*args, **kwargs)
        self.fields['customer'].label_from_instance = self.get_cust_label

    def get_cust_label(self, obj):
        if hasattr(obj, 'indivcust') and obj.cust_type == 'I':
            return f"{obj.indivcust.customer.user.first_name} {obj.indivcust.customer.user.last_name}"
        elif hasattr(obj, 'corpcust') and obj.cust_type == 'C':
            return obj.corpcust.company_name
        return ''

    class Meta:
        model = RentalService
        exclude = ['id', 'vehicle']


class RentalServiceUpdateForm(forms.ModelForm):
    class Meta:
        model = RentalService
        fields = ['pickup_date', 'pickup_street', 'pickup_state', 'dropoff_date',
                  'end_odometer'
                  ]


class VehicleCreationForm(forms.ModelForm):
    class_id = forms.ModelChoiceField(queryset=VClass.objects.all(), label='Type of Vehicle')
    office_id = forms.ModelChoiceField(queryset=Office.objects.all(), label='Office')

    def __init__(self, *args, **kwargs):
        super(VehicleCreationForm, self).__init__(*args, **kwargs)
        self.fields['class_id'].label_from_instance = self.get_class
        self.fields['office_id'].label_from_instance = self.get_office

    def get_class(self, obj):
        return f"{obj.class_name}, ${obj.daily_rate}"

    def get_office(self, obj):
        return f"{obj.address_houseno} {obj.address_street}, {obj.address_city}, {obj.address_zipcode}, {obj.address_state}"

    class Meta:
        model = Vehicle
        exclude = ['id']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ['id', 'invoice']


class FinalizeBookingForm(forms.ModelForm):
    apply_discounts = forms.BooleanField(required=False)
    class Meta:
        model = RentalService
        fields = ['start_odometer', 'end_odometer', 'dropoff_date']

    def __init__(self, *args, **kwargs):
        super(FinalizeBookingForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')

        if instance:
            self.fields['start_odometer'].widget.attrs['placeholder'] = str(instance.start_odometer)
            self.fields['dropoff_date'].widget.attrs['placeholder'] = str(instance.dropoff_date)


class IndDiscountCreationForm(forms.ModelForm):
    class Meta:
        model = IndivDiscount
        exclude = ['id']


class CorpDiscountCreationForm(forms.ModelForm):
    class Meta:
        model = CorpDiscount
        exclude = ['id']

