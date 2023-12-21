from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(unique=True, blank=False, null=False, max_length=50)
    

class Product(models.Model):
    name = models.CharField(unique=True, blank=False, null=False, max_length=50)
    description = models.CharField(blank=False, null=False, max_length=250)
    # category = models.CharField(blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=False, null=False)
    price = models.PositiveIntegerField(blank=False, null=False)
