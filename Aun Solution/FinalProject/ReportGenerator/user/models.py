from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

from user.enums import RoleChoices


class User(AbstractUser):
    email: str = models.EmailField(unique=True)
    username: str = models.CharField(max_length=30, unique=True)
    role: RoleChoices = models.CharField(max_length=30, choices=RoleChoices.choices)
    created_at: datetime = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.email} {self.password} {self.role}"
