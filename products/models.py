from django.db import models
from django.utils.translation import gettext_lazy as _
from categories.models import Category


def upload_to(instance, filename):
    return 'products/{filename}'.format(filename=filename)

# Create your models here.
class Product(models.Model):
    name = models.CharField(unique=True, blank=False, null=False, max_length=50)
    description = models.CharField(blank=False, null=False, max_length=500)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=False, null=False)
    price = models.PositiveIntegerField(blank=False, null=False)
    image = models.ImageField(_("Image"), upload_to=upload_to, default='products/default.jpg')
