# Generated by Django 3.0.6 on 2020-06-11 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.CharField(default='', max_length=100),
        ),
    ]
