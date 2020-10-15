from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

from django.contrib.auth.models import User
from .serializer import *
from .functions import get_tokens_for_user


class SignupViewSet(ViewSet):
    serializer_class = SignupSerializer
    http_method_names = ['post']

    def create(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = get_tokens_for_user(user)
                return Response(token, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginViewSet(ViewSet):
    serializer_class = LoginSerializer
    http_method_names = ['post']

    def create(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(email=serializer.validated_data['email'])
                
                if not user.check_password(serializer.validated_data['password']):
                    return Response({'email': ['Wrong Email or Password.']}, status=status.HTTP_400_BAD_REQUEST)
                
                if not user.is_active:
                    return Response({'email': ['This User is Deactivated By Admin']}, status=status.HTTP_400_BAD_REQUEST)

                token = get_tokens_for_user(user)
                return Response(token, status=status.HTTP_200_OK)

            except User.DoesNotExist:
                return Response({'email': ['Wrong Email or Password']}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)