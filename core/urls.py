
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from authentication.views import UserViewSet

router = routers.DefaultRouter()

router.register(r'api/v1/users', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/users/', include('authentication.urls')),
]
