# Generated by Django 4.1.4 on 2023-02-28 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0014_alter_item_image2_alter_item_image3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='item2_img/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='item3_img/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='item4_img/'),
        ),
    ]