from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from apps.main.views import RegisterView, BicycleListAPIView, RentalBice, RentalBiceHistory, RentalBiceHistoryListAPIView


urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token'),
    path('auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', TokenBlacklistView.as_view(), name='logout'),

    path('bicycles/', BicycleListAPIView.as_view(), name='bicycle_list'),
    path('rental/start/', RentalBice.as_view(), name='rental_start'),
    path('rental/end/', RentalBiceHistory.as_view(), name='rental_end'),
    path('rental/history/', RentalBiceHistoryListAPIView.as_view(), name='rental_history'),


]

