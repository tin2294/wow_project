from django.db import models
from django.contrib.auth.models import User
from .constants import STATES, CUST_TYPE

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
    address_state = models.CharField(choices=STATES, verbose_name="State")
    address_zipcode = models.CharField(max_length=5, verbose_name="Zip Code")
    phone = models.CharField(max_length=10, verbose_name="Phone Number")
    cust_type = models.CharField(choices=CUST_TYPE, null=True)


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

### Vehicle Related models

class Office(models.Model):
    address_houseno = models.IntegerField(null=False, verbose_name="House Number")
    address_street = models.CharField(max_length=30, verbose_name="Street")
    address_city = models.CharField(max_length=30, verbose_name="City")
    address_state = models.CharField(choices=STATES, verbose_name="State")
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
    year = models.IntegerField(max_length=4, verbose_name="Vehicle Model Year")
    lp_state = models.CharField(choices=STATES, verbose_name="License Plate State")
    lp_number = models.CharField(max_length=8, verbose_name="License Plate Number")
    class_id = models.ForeignKey(VClass, on_delete=models.CASCADE)
    office_id = models.ForeignKey(Office, on_delete=models.SET_NULL)

## Rental Service

class RentalService(models.Model):
    pickup_street = models.CharField(max_length=30, verbose_name="Pickup Street")
    pickup_city = models.CharField(max_length=30, verbose_name="Pickup City")
    pickup_state = models.CharField(choices=STATES, verbose_name="Pickup State")
    pickup_country = models.CharField(max_length=30, verbose_name="Pickup Country")
    pickup_zipcode = models.CharField(max_length=5, verbose_name="Pickup Zip Code")
    pickup_date = models.DateTimeField(verbose_name="Pickup Date")
    dropoff_date = models.DateTimeField(verbose_name="Drop Off Date")
    start_odometer = models.IntegerField(verbose_name="Start Odometer Reading")
    end_odometer = models.IntegerField(verbose_name="End Odometer Reading")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, null=True)





