from rest_framework import serializers

from apps.main.models import RentalHistory


class RentalSerializer(serializers.Serializer):
    bike_number = serializers.CharField()


class RentalHistorySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    bicycle = serializers.SerializerMethodField()
    rental_start=serializers.SerializerMethodField()
    rental_end=serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    def get_bicycle(self, obj):
        return obj.bicycle.bike_number

    def get_duration(self, obj):
        return f'{int((obj.rental_end - obj.rental_start).total_seconds() // 60)} min'

    def get_rental_start(self, obj):
        return obj.rental_start.strftime('%Y-%m-%d %H:%M:%S')

    def get_rental_end(self, obj):
        return obj.rental_end.strftime('%Y-%m-%d %H:%M:%S')

    class Meta:
        model = RentalHistory
        fields = ['user', 'bicycle', 'rental_start', 'rental_end', 'duration', 'total_price']