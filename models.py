# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CorpCust(models.Model):
    cust = models.OneToOneField('Customer', models.DO_NOTHING, primary_key=True, db_comment='Customer ID')
    company_name = models.CharField(max_length=30, db_comment='Name of the company')
    company_no = models.CharField(max_length=30, db_comment='Registration number of company')
    emp_id = models.BigIntegerField(db_comment='ID of the employee')
    discid = models.OneToOneField('Discount', models.DO_NOTHING, db_column='discid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corp_cust'


class Customer(models.Model):
    cust_id = models.BigIntegerField(primary_key=True, db_comment='Customer ID')
    address_houseno = models.BigIntegerField(db_comment='House Number in Address')
    address_street = models.CharField(max_length=30, db_comment='Street name in Address')
    address_state = models.CharField(max_length=2, db_comment='State name in Address')
    address_city = models.CharField(max_length=30, db_comment='City name in Address')
    address_zipcode = models.CharField(max_length=5, db_comment='Zipcode of address')
    phone = models.CharField(max_length=10, db_comment='PHONE NUMBER')
    cust_type = models.CharField(max_length=1, db_comment='Type of Customer')

    class Meta:
        managed = False
        db_table = 'customer'
        db_table_comment = 'Customers'


class Discount(models.Model):
    discid = models.BigIntegerField(primary_key=True, db_comment='Discount Coupon ID')
    percentage = models.DecimalField(max_digits=7, decimal_places=2, db_comment='Percentage of discount in decimals')
    disc_type = models.CharField(max_length=8, blank=True, null=True, db_comment='Type of Discount')

    class Meta:
        managed = False
        db_table = 'discount'
        db_table_comment = 'Discount coupons'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class IndivCust(models.Model):
    cust = models.OneToOneField(Customer, models.DO_NOTHING, primary_key=True, db_comment='Customer ID')
    fname = models.CharField(max_length=30, db_comment='First Name of individual customer')
    lname = models.CharField(max_length=30, db_comment='Last Name of Individual Customer')
    licenseno = models.CharField(max_length=15, db_comment='Licence Number of Individual customer')
    insurance_co = models.CharField(max_length=30, db_comment='Insurance company name')
    insurancep_no = models.CharField(max_length=30, db_comment='Insurance policy number')

    class Meta:
        managed = False
        db_table = 'indiv_cust'


class IndividualDisc(models.Model):
    discid = models.OneToOneField(Discount, models.DO_NOTHING, db_column='discid', primary_key=True, db_comment='Discount Coupon ID')
    start_date = models.DateTimeField(db_comment='Start date of validity of coupon')
    end_date = models.DateTimeField(db_comment='End date of validity of coupon')
    cust = models.ForeignKey(IndivCust, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'individual_disc'


class InvDisc(models.Model):
    invoice = models.ForeignKey('Invoice', models.DO_NOTHING, blank=True, null=True, db_comment='Invoice ID')
    discid = models.ForeignKey(Discount, models.DO_NOTHING, db_column='discid', blank=True, null=True, db_comment='Discount ID')

    class Meta:
        managed = False
        db_table = 'inv_disc'
        db_table_comment = 'Associate Table invoice discount'


class Invoice(models.Model):
    invoice_id = models.BigIntegerField(primary_key=True, db_comment='Invoice ID')
    invoice_date = models.DateTimeField(db_comment='Invoice date')
    service = models.ForeignKey('RentalService', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'invoice'
        db_table_comment = 'Invoices'


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


class Payment(models.Model):
    payment_id = models.BigIntegerField(primary_key=True, db_comment='Payment ID')
    card_number = models.CharField(max_length=20, db_comment='Card number (for gift, credit or debit card)')
    payment_method = models.CharField(max_length=1, db_comment='Payment method, which can only be G, C, D')
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment'


class RentalService(models.Model):
    service_id = models.IntegerField(primary_key=True, db_comment='Service ID')
    pickup_street = models.CharField(max_length=30, db_comment='Pick up street name')
    pickup_state = models.CharField(max_length=2, db_comment='State of pickup (abbreviated)')
    pickup_country = models.CharField(max_length=30, db_comment='Country of pickup')
    pickup_zipcode = models.CharField(max_length=5, db_comment='Zip code of pickup')
    pickup_date = models.DateTimeField(db_comment='Pickup date')
    dropoff_date = models.DateTimeField(db_comment='Drop off date')
    start_odometer = models.BigIntegerField(db_comment='Starting odometer read')
    end_odometer = models.BigIntegerField(db_comment='End odometer read')
    vehicle = models.ForeignKey('Vehicle', models.DO_NOTHING, blank=True, null=True)
    cust = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rental_service'
        db_table_comment = 'Rental services'


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
