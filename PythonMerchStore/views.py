from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from PythonMerchStore.models import Product, ProductEditForm
from django import forms



def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'index.html', context)



def Product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'product.html', context)



def edit_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = ProductEditForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product_id)
    else:
        form = ProductEditForm(instance=product)
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'update.html', context)



def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('index')



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'image_url', 'description']



def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)