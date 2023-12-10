from django.db import models
from datetime import datetime # this is intentional don't change it to import datetime
from django.contrib.auth.models import User
from .constants import STATES, CUST_TYPE, PAYMENT_METHOD_TYPE

### User-related models

"""
Implicit definition of User

Fields in User:
    - id (primary key)
    - first_name
    - last_name
    - email
    - password1
    - password2
    - is_staff
    - is_admin
    - is_superuser
    - is_active
    
"""
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_houseno = models.IntegerField(null=False, verbose_name="House Number")
    address_street = models.CharField(max_length=30, verbose_name="Street")
    address_city = models.CharField(max_length=30, verbose_name="City")
    address_state = models.CharField(max_length=2, choices=STATES, verbose_name="State")
    address_zipcode = models.CharField(max_length=5, verbose_name="Zip Code")
    phone = models.CharField(max_length=10, verbose_name="Phone Number")
    cust_type = models.CharField(max_length=1, choices=CUST_TYPE, null=True)


class CorpCust(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30, verbose_name="Company Name")
    company_number = models.CharField(max_length=30, null=True, verbose_name="Company Number")
    emp_id = models.IntegerField(null=True, verbose_name="Internal Employee ID Number")


class IndivCust(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    license_no = models.CharField(max_length=15, verbose_name="Driver's License Number")
    insurance_co = models.CharField(max_length=30, verbose_name="Insurance Provider")
    insurance_policy_num = models.CharField(max_length=30, verbose_name="Insurance Policy Number")

class CorpDiscount(models.Model):
    customer = models.OneToOneField(CorpCust, on_delete=models.CASCADE, null=True, blank=True)
    percentage = models.DecimalField(default=0, max_digits=2, decimal_places=2)

class IndivDiscount(models.Model):
    customer = models.ForeignKey(IndivCust, on_delete=models.CASCADE, null=True, blank=True)
    percentage = models.DecimalField(default=0, max_digits=2, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

### Vehicle Related models

class Office(models.Model):
    address_houseno = models.IntegerField(null=False, verbose_name="House Number")
    address_street = models.CharField(max_length=30, verbose_name="Street")
    address_city = models.CharField(max_length=30, verbose_name="City")
    address_state = models.CharField(max_length=2, choices=STATES, verbose_name="State")
    address_zipcode = models.CharField(max_length=5, verbose_name="Zip Code")
    phone = models.CharField(max_length=10, verbose_name="Phone Number")


class VClass(models.Model):
    class_name = models.CharField(max_length=30, verbose_name="Vehicle Class")
    daily_rate = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Daily Rate")
    daily_mileage = models.IntegerField(verbose_name="Daily Allotted Mileage")
    overage_rate = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Fee Per Mile for Overages")


class Vehicle(models.Model):
    vin = models.CharField(max_length=30, verbose_name="VIN")
    make = models.CharField(max_length=30, verbose_name="Vehicle Make")
    model = models.CharField(max_length=30, verbose_name="Vehicle Model")
    year = models.IntegerField(verbose_name="Vehicle Model Year")
    lp_state = models.CharField(max_length=2, choices=STATES, verbose_name="License Plate State")
    lp_number = models.CharField(max_length=8, verbose_name="License Plate Number")
    vclass = models.ForeignKey(VClass, on_delete=models.CASCADE)
    office = models.ForeignKey(Office, on_delete=models.SET_NULL, blank=True, null=True)

## Rental Service

class RentalService(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, null=True)
    pickup_street = models.CharField(max_length=30, verbose_name="Pickup Street")
    pickup_city = models.CharField(max_length=30, verbose_name="Pickup City")
    pickup_state = models.CharField(max_length=2, choices=STATES, verbose_name="Pickup State")
    pickup_country = models.CharField(max_length=30, verbose_name="Pickup Country")
    pickup_zipcode = models.CharField(max_length=5, verbose_name="Pickup Zip Code")
    pickup_date = models.DateTimeField(verbose_name="Pickup Date")
    dropoff_date = models.DateTimeField(verbose_name="Drop Off Date")
    start_odometer = models.IntegerField(verbose_name="Start Odometer Reading")
    end_odometer = models.IntegerField(verbose_name="End Odometer Reading", null=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # When a RentalService instance concludes (is set to inactive), create an invoice for the trip
        # based on start and end odometer
        if not self.is_active:
            Invoice.objects.create(service=self, invoice_date=datetime.now())


class Invoice(models.Model):
    service = models.ForeignKey(RentalService, on_delete=models.SET_NULL, null=True, blank=True)
    invoice_date = models.DateTimeField(verbose_name="Invoice Date")


class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.DO_NOTHING, null=True)
    card_number = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=1, choices=PAYMENT_METHOD_TYPE)


class InvoiceCorpDiscount(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    discount = models.ForeignKey(CorpDiscount, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['invoice', 'discount']


class InvoiceIndivDiscount(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    discount = models.ForeignKey(IndivDiscount, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['invoice', 'discount']


