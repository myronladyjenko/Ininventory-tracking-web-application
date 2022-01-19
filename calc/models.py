from django.db import models

class Destination(models.Model):

    product_name = models.CharField(max_length=100) 
    price = models.FloatField()
    quantity = models.IntegerField()

# Create your models here.
