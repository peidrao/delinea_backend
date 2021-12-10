from django.urls import path, include
from rest_framework import routers

from .views import ProductViewSet


router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')

urlpatterns = [
    path(
        "",
        include(
            (router.urls, 'product'),
            namespace='products_urls',
        ),
    ),

]
