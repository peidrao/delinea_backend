# import jwt

from django.conf import settings
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    queryset = User.objects.filter(is_active=True)


@api_view(['POST'])
def create_user(request):
    if request.data['password'] == '':
        message = {'text': 'Você precisa de uma senha!'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.create(
            username=request.data['username'],
            email=request.data['email'],
            password=make_password(request.data['password']),
            is_staff=request.data['is_staff'],
            is_active=request.data['is_active'],
            is_superuser=request.data['is_superuser']
        )
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except:
        message = {'text': 'Email já está cadastrado'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
