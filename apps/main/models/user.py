from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


class User(AbstractUser):
    def get_tokens(self):
        access_token = AccessToken.for_user(self)
        refresh_token = RefreshToken.for_user(self)
        return {
            "access": str(access_token),
            "refresh": str(refresh_token)
        }
