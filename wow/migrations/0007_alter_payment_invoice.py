# Generated by Django 4.2.8 on 2023-12-10 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wow", "0006_rentalservice_is_active_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="invoice",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="wow.invoice",
            ),
        ),
    ]