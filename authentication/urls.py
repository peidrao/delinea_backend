from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.create_user, name='register_user'),
    # path('users/', views.get_users, name='get_users'),
    # path('update/', views.update_user, name='update_user')
]
