from django.contrib import admin
from apps.main.models import Bicycle, Rental, RentalHistory

admin.site.register(Bicycle)
admin.site.register(Rental)
admin.site.register(RentalHistory)
