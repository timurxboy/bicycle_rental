from django.urls import path, include
from apps.main.views import BicycleListAPIView, RentalBice, RentalBiceHistory, RentalBiceHistoryListAPIView

urlpatterns = [
    path('bicycles/', BicycleListAPIView.as_view(), name='bicycle_list'),
    path('rental/start/', RentalBice.as_view(), name='rental_start'),
    path('rental/end/', RentalBiceHistory.as_view(), name='rental_end'),
    path('rental/history/', RentalBiceHistoryListAPIView.as_view(), name='rental_history'),
]

