# Generated by Django 4.1.4 on 2023-02-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0018_remove_item_quantity_booking_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='condition',
            field=models.IntegerField(null=True),
        ),
    ]
