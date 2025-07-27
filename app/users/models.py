import uuid
from typing import List

from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    uuid_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, null=False)
    email = models.EmailField(unique=True)
    username = models.CharField(default='', max_length=150, unique=True, blank=True, null=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: List[str] = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
