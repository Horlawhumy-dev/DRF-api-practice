from django.db import models

# Create your models here.
class Employee(models.Model):
    fulllname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=20)