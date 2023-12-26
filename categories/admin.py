from django.contrib import admin
from categories.models import Category

# Register your models here.
@admin.register(Category)
class CategoryModel(admin.ModelAdmin):
    list_display = ('id', 'name')