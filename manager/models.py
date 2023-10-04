from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Worker(AbstractUser):
    position = models.ForeignKey(
        "Position", on_delete=models.SET_NULL, related_name="workers",
        null=True, blank=True
    )


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name",]


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name", ]


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=255, choices=[
        ("Ur", "Urgent"), ("H", "High"), ("M", "Medium"), ("L", "Low"),
    ])
    task_type = models.ForeignKey(
        "TaskType", on_delete=models.CASCADE, related_name="tasks"
    )
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="tasks"
    )

    class Meta:
        ordering = ["-deadline"]

    def __str__(self) -> str:
        return f"{self.name} (deadline:{self.deadline})"
