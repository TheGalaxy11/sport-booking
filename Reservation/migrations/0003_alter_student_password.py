# Generated by Django 4.1.4 on 2023-02-27 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0002_alter_student_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.TextField(default='123456', max_length=25, null=True, verbose_name='Password'),
        ),
    ]
