# Generated by Django 5.0.6 on 2024-07-04 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_bicycle_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentalhistory',
            old_name='price',
            new_name='total_price',
        ),
    ]
