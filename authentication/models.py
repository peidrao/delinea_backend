from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER = (
        (1, 'Homem'),
        (2, 'Mulher'),
        (3, 'Outro'),
    )

    gender = models.SmallIntegerField(
        choices=GENDER, verbose_name='Gênero', help_text="1 - Homem, 2 - Mulher, 3 - Outro", null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.first_name
