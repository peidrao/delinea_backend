from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            'last_name',
            'is_superuser',
            'is_staff',
            "email",
            "password",
            "is_active",
            "gender",
        )
