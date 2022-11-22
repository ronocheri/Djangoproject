from django.db import models

#inherit from Model class, will have the capabilities to get and updata data on DB
class Product(models.Model):
    name= models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    image_url=models.CharField(max_length=2083)

class Offer(models.Model):
    code= models.CharField(max_length=10)
    description=models.CharField(max_length=255)
    discount=models.FloatField()
