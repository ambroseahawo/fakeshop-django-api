from django.urls import path
from categories.views import CategoriesListView, CategoryDetailView

app_name = 'categories'

urlpatterns = [
    path('<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('', CategoriesListView.as_view(), name="categories_index")
]
