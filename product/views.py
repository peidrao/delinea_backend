from rest_framework.response import Response
from rest_framework import viewsets, status, filters
from .models import Product
from .serializers import ProductSerializer, ProductAllSerializer
from .filters import ProductTitleFilter, ProductPriceFilter
from .permissions import ProductPermission, IsOwner


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner, ProductPermission]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [
        filters.SearchFilter,
        ProductPriceFilter,
        ProductTitleFilter,
    ]
    search_fields = (
        'title',
        'price'
    )
    
    # def destroy(self, request, *args, **kwargs):
    #     try:
    #         instance = self.get_object()
    #         self.perform_destroy(instance)
    #     except:
    #     return Response(status=status.HTTP_204_NO_CONTENT)

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

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(owner=request.user)
        serializer = ProductAllSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductAllSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
