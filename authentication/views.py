from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .permissions import IsSuperUser, IsOwner
from django.contrib.auth.hashers import make_password


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            User.objects.create(
                username=data['username'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                is_active=data['is_active'],
                is_staff=data['is_staff'],
                is_superuser=data['is_superuser'],
                email=data['email'],
                password=make_password(data['password'])
            )
            data.pop('password')
            data.pop('is_staff')
            data.pop('is_superuser')
            data.pop('is_active')

            return Response(data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_403_FORBIDDEN)

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsSuperUser, ]
        elif self.action == 'retrieve':
            self.permission_classes = [IsOwner]
        return super(self.__class__, self).get_permissions()

    def update(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=kwargs['pk'])
            user.username = request.data['username']
            user.is_active = request.data['is_active']
            user.first_name = request.data['first_name']
            user.last_name = request.data['last_name']
            user.is_superuser = request.data['is_superuser']
            user.is_staff = request.data['is_staff']
            user.email = request.data['email']
            user.password = make_password(request.data['email'])
            user.save()
            return Response({'message': 'User updated successfully'}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
