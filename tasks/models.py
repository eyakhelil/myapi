# tasks/models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

from django.db import models

class Entity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FieldDefinition(models.Model):
    entity = models.ForeignKey(Entity, related_name='fields', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.field_type})"

class IntegrationLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"{self.timestamp} - {self.entity.name} - {self.action}"
