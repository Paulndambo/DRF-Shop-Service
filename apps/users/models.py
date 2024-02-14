from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.core.constants import GENDER_CHOICES, USER_ROLES
from apps.core.models import AbstractBaseModel


# Create your models here.
class User(AbstractUser, AbstractBaseModel):
    role = models.CharField(max_length=255, choices=USER_ROLES)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.username
