from django.db.models import fields
from rest_framework import serializers
from .models import Product
from authentication.models import User


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('title', 'content', 'price')

    
    def create(self, validated_data):

        return super().create(validated_data)