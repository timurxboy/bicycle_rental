from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password, make_password
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from apps.main.serializers import LoginSerializer, RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

User = get_user_model()


@extend_schema(tags=['auth'])
class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        try:
            user = User.objects.get(username=username)

            if check_password(password, user.password):
                access_token = AccessToken.for_user(user)
                refresh_token = RefreshToken.for_user(user)

                tokens = {
                    'access': access_token.__str__(),
                    'refresh': refresh_token.__str__(),
                    'user_id': user.id,
                    'first_name': user.first_name,
                    'last_name': user.last_name
                }
                return self.send_response(tokens, status.HTTP_200_OK)
            else:
                return self.send_response(
                    {"message": "Your password is incorrect"},
                    status.HTTP_400_BAD_REQUEST
                )
        except User.DoesNotExist:
            return self.send_response(
                {"message": "Couldn't find your account"},
                status.HTTP_400_BAD_REQUEST
            )

    def send_response(self, data, status_code):
        return Response(data=data, status=status_code)


class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        first_name = serializer.validated_data['first_name']
        last_name = serializer.validated_data['last_name']
        email = serializer.validated_data['email']


        if User.objects.get(username=username):
            return self.send_response({f"{username}": "user with this username already exists."}, status.HTTP_400_BAD_REQUEST)

        else:
            User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email,

            )

            return self.send_response('', status.HTTP_201_CREATED)

    def send_response(self, data, status_code):
        return Response(data=data, status=status_code)

