# Generated by Django 4.1.4 on 2023-02-28 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0012_alter_booking_itemcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image2',
            field=models.ImageField(null='NOT NULL', upload_to='item2_img/'),
            preserve_default='NOT NULL',
        ),
        migrations.AddField(
            model_name='item',
            name='image3',
            field=models.ImageField(null='NOT NULL', upload_to='item3_img/'),
            preserve_default='NOT NULL',
        ),
        migrations.AddField(
            model_name='item',
            name='image4',
            field=models.ImageField(null='NOT NULL', upload_to='item4_img/'),
            preserve_default='NOT NULL',
        ),
    ]
