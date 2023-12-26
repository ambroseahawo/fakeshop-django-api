from django.contrib import admin
from categories.models import Category

# Register your models here.
@admin.register(Category)
class CategoryModel(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_filter = ('name',)
    search_fields = ('name',)