from drf_yasg.openapi import Response
from rest_framework import permissions

from product.models import Product


class ProductPermission(permissions.BasePermission):

    # edit_methods = ("PUT", "PATCH", 'GET')

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False

        if request.method == 'GET':
            if Product.objects.filter(owner=request.user).exists():
                return True

        if request.method == 'POST':
            return True

    def has_object_permission(self, request, view, obj):
        if Product.objects.filter(owner=request.user).exists():
            return True

        return False
