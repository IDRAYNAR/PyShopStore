from django.db import models
from django import forms



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083,default="")
    description = models.TextField(default="")
    
    def __str__(self):
        return self.name



class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'image_url', 'description']



