# Generated by Django 5.0.6 on 2024-07-04 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicycle',
            name='rental_status',
            field=models.CharField(choices=[('available', 'Available'), ('rented', 'Rented')], default='available', max_length=12, verbose_name='Rental Status'),
        ),
    ]
