from django.db import models
from django.contrib.auth.models import User
from .constants import STATES, CUST_TYPE

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_houseno = models.IntegerField(null=False, verbose_name="House Number")
    address_street = models.CharField(max_length=30, verbose_name="Street")
    address_city = models.CharField(max_length=30, verbose_name="City")
    address_state = models.CharField(choices=STATES, verbose_name="State")
    address_zipcode = models.CharField(max_length=5)
    phone = models.CharField(max_length=10)
    cust_type = models.CharField(choices=CUST_TYPE)




