from django.urls import path
from . import views



app_name = 'PythonMerchStore'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/<int:product_id>/', views.Product_detail, name='product_detail'),
    path('products/<int:product_id>/edit', views.edit_product, name='edit_product'),
    path('products/<int:product_id>/delete', views.delete_product, name='delete_product'),
    path('products/create/', views.create_product, name='create_product'),
]


