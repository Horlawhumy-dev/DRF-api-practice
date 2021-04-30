from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=256, null=True)
    completed = models.BooleanField(null=True)

    def __str__(self):
        return self.title