# Generated by Django 4.0.2 on 2022-03-19 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0016_alter_car_plate_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='tabs',
            new_name='_tabs',
        ),
    ]
