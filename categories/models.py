from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(unique=True, blank=False, null=False, max_length=50)
    
    class Meta:
        verbose_name_plural = 'categories'
        
    def __str__(self) -> str:
        return self.name