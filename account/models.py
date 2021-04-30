from django.db import models
from datetime import timezone

# Create your models here.

# positions = {
#     'Jr': 'Junior',
#     'Sr': 'Senior',
#     'Int': 'Intermediate'
#     }

# class Position(models.Model):
#     title = models.Choices(positions)

#     def __str__(self):
#         return self.title

class UserAccount(models.Model):
    name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    password2 = models.CharField(max_length=100, null=True)
    # date_created = models.DateTimeField(default=timezone)

    def __str__(self):
        return self.username
