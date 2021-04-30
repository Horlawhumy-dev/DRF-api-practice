from django.db import models

# Create your models here.
class UserForm(models.Model):
    username = models.CharField(max_length=120)
    email = models.EmailField(max_length=200)

class Something(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
 
    

