from django.db import models




class StatusChoices (models.TextChoices):
    in_progress = "in_progress","InProgress"
    completed = "completed","Completed"
    failed = "failed", "Failed"