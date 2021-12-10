from rest_framework.response import Response
from rest_framework import serializers, viewsets, status, filters
from .models import Product
from .serializers import ProductSerializer, ProductAllSerializer
from .filters import ProductTitleFilter, ProductPriceFilter
from .permissions import ProductPermission


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [ProductPermission]
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
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = Product.objects.create(
                title=serializer.data['title'],
                content=serializer.data['content'],
                price=serializer.data['price'],
                owner=request.user
            )
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        serializer = ProductAllSerializer(
            self.queryset.filter(owner=request.user), many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Exception as e:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = ProductAllSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
