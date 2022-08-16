from unicodedata import name
from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_done = models.BooleanField()

    def __str__(self):
        return self.name
    