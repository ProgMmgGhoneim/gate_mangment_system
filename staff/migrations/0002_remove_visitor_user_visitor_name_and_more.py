# Generated by Django 4.0.2 on 2022-02-26 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='user',
        ),
        migrations.AddField(
            model_name='visitor',
            name='name',
            field=models.CharField(default=1, max_length=256, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='visitor',
            name='job_title',
            field=models.CharField(max_length=256, verbose_name='Job Title'),
        ),
    ]
