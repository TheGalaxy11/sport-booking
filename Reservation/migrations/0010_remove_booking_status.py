# Generated by Django 4.1.4 on 2023-02-28 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0009_alter_item_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='status',
        ),
    ]