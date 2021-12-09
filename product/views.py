from rest_framework.response import Response
from rest_framework import viewsets, status, filters
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductTitleFilter, ProductPriceFilter


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (
        ProductPriceFilter,
        ProductTitleFilter,
        filters.SearchFilter,
    )
    search_fields = (
        'title',
        'price'
    )

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
