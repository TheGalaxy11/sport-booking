# Generated by Django 4.1.4 on 2023-02-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0004_alter_student_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='password',
            new_name='password1',
        ),
        migrations.AddField(
            model_name='student',
            name='password2',
            field=models.TextField(default='NULL', max_length=25, verbose_name='Password'),
        ),
    ]
