# Generated by Django 4.0.2 on 2022-03-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_apikey'),
    ]

    operations = [
        migrations.AddField(
            model_name='apikey',
            name='type',
            field=models.CharField(default='Bearer', max_length=50, verbose_name='type'),
            preserve_default=False,
        ),
    ]
