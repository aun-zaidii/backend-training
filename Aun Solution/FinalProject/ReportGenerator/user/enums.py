from django.db import models


class RoleChoices(models.TextChoices):
    admin = "admin", "Admin"
    moderator = "moderator", "Moderator"
    viewer = "viewer", "Viewer"
