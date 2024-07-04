from django.db import models
from django.contrib.auth.models import User
from apps.main.models.bicycle import Bicycle


class Rental(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bicycle = models.OneToOneField(Bicycle, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}({self.created_at.strftime('%Y-%m-%d %H:%M:%S')})'


class RentalHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bicycle = models.ForeignKey(Bicycle, on_delete=models.CASCADE)
    rental_start = models.DateTimeField()
    rental_end = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

