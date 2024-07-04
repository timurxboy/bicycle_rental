from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.main.serializers import UserRegisterSerializer


class RegisterView(APIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
