from rest_framework import serializers

from apps.main.models import Bicycle


class BicycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bicycle
        fields = '__all__'