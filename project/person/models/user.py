from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=300)
    birth_date = models.DateTimeField(null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_phone_or_email",
                check=(
                    models.Q(phone__isnull=False) 
                    | models.Q(email__isnull=False)
                ),
            )
        ]

    def __str__(self) -> str:
        return self.name
