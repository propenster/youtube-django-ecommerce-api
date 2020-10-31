from django.urls import path
from .views import ListCategory, DetailCategory, ListBook, DetailBook, ListProduct, DetailProduct
urlpatterns = [
    path('categories', ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),
    path('books', ListBook.as_view(), name='books'),
    path('books/<int:pk>/', DetailBook.as_view(), name='singlebook'),

    path('products', ListProduct.as_view(), name='products'),
    path('products/<int:pk>/', DetailProduct.as_view(), name='singleproduct'),
]
