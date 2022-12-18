from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from PythonMerchStore.models import Product

def index(request):
    context={}
    template = loader.get_template('index.html')
    products = Product.objects.all()
    context["products"] = products
    return HttpResponse(template.render(context, request))

def Product_detail(request, product_id):
    context={}
    template = loader.get_template('product.html')
    product = Product.objects.get(pk=product_id)
    context["product"] = product
    return HttpResponse(template.render(context, request))