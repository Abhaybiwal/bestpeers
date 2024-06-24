from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    return render(request,'shop/index.html')


def about(request):
    return render(request,'shop/about.html')


def contact(request):
    return HttpResponse("we are at contact")


def tracker(request):
    return HttpResponse("we are at tracker")


def search(request):
    return HttpResponse("we are at search")


def prodeuct_view(request):
    products = Product.objects.all()
    context = {
        'product_list': products
    }
    return render(request,'shop/product.html',context)


def checkout(request):
    return HttpResponse("we are at checkout")