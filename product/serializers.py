from django.db.models import fields
from rest_framework import serializers
from .models import Product
from authentication.models import User


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('title', 'content', 'price')


class ProductAllSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # owner_username = serializers.CharField(source='owner.username')
    class Meta:
        model = Product
        fields = "__all__"
