from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(unique=True, blank=False, null=False, max_length=50)