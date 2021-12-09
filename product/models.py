from django.db import models
from django.db.models.deletion import DO_NOTHING

from authentication.models import User
# Create your models here.

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=DO_NOTHING, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    price = models.FloatField()


    def __str__(self) -> str:
        return self.title