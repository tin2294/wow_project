from django.db import models

# Create your models here.


class Employee(models.Model):
    employee_id = models.BigIntegerField(primary_key=True, db_comment='Employee ID')
    fname = models.CharField(max_length=30, db_comment='First Name of employee')
    lname = models.CharField(max_length=30, db_comment='Last Name of employee')
    email = models.CharField(max_length=25, db_comment='email')
    phone = models.CharField(max_length=10, db_comment='phone number')
    emp_role = models.CharField(max_length=25, blank=True, null=True, db_comment='role of employee')

    class Meta:
        managed = False
        db_table = 'employee'


class Vclass(models.Model):
    classid = models.BigIntegerField(primary_key=True, db_comment='Vehicle Class ID')
    class_name = models.CharField(max_length=30, db_comment='Vehicle class name')
    daily_rate = models.DecimalField(max_digits=7, decimal_places=2, db_comment='Daily rate of vehicle class')
    daily_mileage = models.BigIntegerField(db_comment='Daily mileage of vehicle class')
    overage_rate = models.DecimalField(max_digits=7, decimal_places=2, db_comment='Overage rate for vehicle class')

    class Meta:
        managed = False
        db_table = 'vclass'
        db_table_comment = 'Vehicle classes'


class Office(models.Model):
    office_id = models.BigIntegerField(primary_key=True, db_comment='Rental Office ID')
    address_houseno = models.BigIntegerField(db_comment='Number of house in address')
    address_street = models.CharField(max_length=30, db_comment='Street name of address')
    address_state = models.CharField(max_length=2, db_comment='State of the address abbreviated')
    address_city = models.CharField(max_length=30, db_comment='City of address')
    address_zipcode = models.CharField(max_length=5, db_comment='Zipcode of address')
    phone = models.CharField(max_length=10, db_comment='Phone of office')

    class Meta:
        managed = False
        db_table = 'office'
        db_table_comment = 'Rental offices'


class Vehicle(models.Model):
    vehicle_id = models.BigIntegerField(primary_key=True, db_comment='ID Number of Vehicle')
    vin = models.CharField(max_length=30, db_comment='Vehicle Identification Number')
    make = models.CharField(max_length=30, db_comment='Make of vehicle')
    model = models.CharField(max_length=30, db_comment='Model of vehicle')
    year = models.BigIntegerField(db_comment='Year of the car')
    lp_state = models.CharField(max_length=2, db_comment='License Plate State (abbreviated)')
    lp_number = models.CharField(max_length=8, db_comment='License Plate number')
    classid = models.ForeignKey(Vclass, models.DO_NOTHING, db_column='classid')
    office = models.ForeignKey(Office, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vehicle'
        db_table_comment = 'Vehicles'
