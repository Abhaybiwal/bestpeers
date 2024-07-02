from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Product,Contact,Cart
from math import ceil

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    # data = Product.objects.filter(category = "cat")
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])


    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request,'shop/about.html')


def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    # elif request.method=="GET":
    #     print(request.GET.get("a"))
    return render(request, "shop/contact.html")


def tracker(request):
    return render(request,'shop/tracker.html')


def search(request):
    return HttpResponse("we are at search")


def prodeuct_view(request,myid):
    product = Product.objects.filter(id=myid)
    context = {
        'product': product[0]
    }
    return render(request,'shop/product.html',context)


def checkout(request):
    return render(request,'shop/checkout.html')