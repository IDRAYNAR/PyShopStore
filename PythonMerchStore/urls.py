from django.urls import path
from . import views

app_name = 'PythonMerchStore'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/<int:product_id>', views.Product_detail, name='product'),
]
