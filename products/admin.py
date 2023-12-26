from django.contrib import admin
from products.models import Product

# Register your models here.
@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'id')
    list_filter = ('name', 'category', 'price')
    search_fields = ('name', 'category', 'price')
