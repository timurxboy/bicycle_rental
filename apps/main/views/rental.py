import datetime

from rest_framework import views, permissions, request, status, generics
from rest_framework.response import Response

from apps.main.serializers import RentalSerializer, RentalHistorySerializer
from apps.main.models import Rental, RentalHistory, Bicycle


class RentalBice(views.APIView):
    serializer_class = RentalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        bike_number = serializer.validated_data['bike_number']
        user = request.user

        if bicycle := Bicycle.objects.filter(bike_number=bike_number).first():
            if rental := Rental.objects.filter(user=user):
                return Response("You can't take more than one bike", status=status.HTTP_400_BAD_REQUEST)
            else:
                rental = Rental.objects.create(
                    user=user,
                    bicycle=Bicycle.objects.get(bike_number=bike_number)
                )
                rental.save()
                response_data = {
                    'user': user.username,
                    'bike_number': bike_number,
                    'rental_start': rental.created_at.strftime('%Y-%m-%d %H:%M:%S')
                }
                return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response('Bicycle not found', status=status.HTTP_404_NOT_FOUND)


class RentalBiceHistory(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        rental_end = datetime.datetime.now().astimezone(datetime.timezone.utc)
        user = request.user
        if rental := Rental.objects.filter(user=user).first():
            rental_history = RentalHistory.objects.create(
                user=user,
                bicycle=rental.bicycle,
                rental_start=rental.created_at,
                rental_end=rental_end,
                total_price=(rental_end - rental.created_at).total_seconds() // 60 * float(rental.bicycle.price)
            )
            rental_history.save()
            rental.delete()
            response_data = {
                'total_price': rental_history.total_price,
                'time (min)': (rental_history.rental_end - rental_history.rental_start).total_seconds() // 60
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response('Rental bicycle does not exist', status=status.HTTP_404_NOT_FOUND)


class RentalBiceHistoryListAPIView(generics.ListAPIView):
    serializer_class = RentalHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RentalHistory.objects.filter(user=self.request.user).order_by('-id')
