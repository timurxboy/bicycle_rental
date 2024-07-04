from rest_framework import generics, permissions

from apps.main.models import Bicycle
from apps.main.serializers import BicycleSerializer


class BicycleListAPIView(generics.ListAPIView):
    queryset = Bicycle.objects.filter(rental_status='available')
    serializer_class = BicycleSerializer
    permission_classes = [permissions.IsAuthenticated]
