from django.db import models


class Bicycle(models.Model):
    BIKE_TYPES = [
        ('urban', 'Urban'),
        ('mountain', 'Mountain'),
        ('road', 'Road'),
    ]

    RENTAL_STATUS = [
        ('available', 'Available'),
        ('rented', 'Rented')
    ]

    bike_number = models.CharField(max_length=50, unique=True, verbose_name="Bike Number")
    location = models.CharField(max_length=255, verbose_name="Location")

    bike_type = models.CharField(max_length=10, choices=BIKE_TYPES, verbose_name="Bike Type")
    rental_status = models.CharField(max_length=12, choices=RENTAL_STATUS, default='available',
                                     verbose_name="Rental Status")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
            return f"{self.bike_number} - {self.bike_type}"
