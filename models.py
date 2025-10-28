from django.db import models

# Create your models here.

class Laptops(models.Model):
    name=models.CharField(max_length=20)
    model_name=models.CharField(max_length=10)
    cost=models.IntegerField()

