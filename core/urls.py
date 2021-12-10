
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# from authentication.views import UserViewSet
# from product.views import ProductViewSet

# router = routers.DefaultRouter()

# router.register(r'api/v1/users', UserViewSet, basename='user')
# router.register(r'api/v1/products', ProductViewSet, basename='product')


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    path('products/', include('product.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),

]
