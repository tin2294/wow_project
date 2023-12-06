# Generated by Django 5.0 on 2023-12-06 02:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wow", "0002_office_vclass_vehicle"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "cust_id",
                    models.BigIntegerField(
                        db_comment="Customer ID", primary_key=True, serialize=False
                    ),
                ),
                (
                    "address_houseno",
                    models.BigIntegerField(db_comment="House Number in Address"),
                ),
                (
                    "address_street",
                    models.CharField(
                        db_comment="Street name in Address", max_length=30
                    ),
                ),
                (
                    "address_state",
                    models.CharField(db_comment="State name in Address", max_length=2),
                ),
                (
                    "address_city",
                    models.CharField(db_comment="City name in Address", max_length=30),
                ),
                (
                    "address_zipcode",
                    models.CharField(db_comment="Zipcode of address", max_length=5),
                ),
                ("phone", models.CharField(db_comment="PHONE NUMBER", max_length=10)),
                (
                    "cust_type",
                    models.CharField(db_comment="Type of Customer", max_length=1),
                ),
            ],
            options={
                "db_table": "customer",
                "db_table_comment": "Customers",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="RentalService",
            fields=[
                (
                    "service_id",
                    models.IntegerField(
                        db_comment="Service ID", primary_key=True, serialize=False
                    ),
                ),
                (
                    "pickup_street",
                    models.CharField(db_comment="Pick up street name", max_length=30),
                ),
                (
                    "pickup_state",
                    models.CharField(
                        db_comment="State of pickup (abbreviated)", max_length=2
                    ),
                ),
                (
                    "pickup_country",
                    models.CharField(db_comment="Country of pickup", max_length=30),
                ),
                (
                    "pickup_zipcode",
                    models.CharField(db_comment="Zip code of pickup", max_length=5),
                ),
                ("pickup_date", models.DateTimeField(db_comment="Pickup date")),
                ("dropoff_date", models.DateTimeField(db_comment="Drop off date")),
                (
                    "start_odometer",
                    models.BigIntegerField(db_comment="Starting odometer read"),
                ),
                (
                    "end_odometer",
                    models.BigIntegerField(db_comment="End odometer read"),
                ),
            ],
            options={
                "db_table": "rental_service",
                "db_table_comment": "Rental services",
                "managed": False,
            },
        ),
    ]