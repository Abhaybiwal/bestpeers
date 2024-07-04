# views.py
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, TemplateView, DetailView, FormView, View
from django.http import HttpResponse,JsonResponse
from .models import *
from .forms import ContactForm
from math import ceil
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


class IndexView(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'allProds'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        allProds = []
        catprods = Product.objects.values('category', 'id')
        cats = {item['category'] for item in catprods}
        for cat in cats:
            prod = Product.objects.filter(category=cat)
            n = len(prod)
            nSlides = n // 4 + ceil((n / 4) - (n // 4))
            allProds.append([prod, range(1, nSlides), nSlides])
        context['allProds'] = allProds
        return context

class AboutView(TemplateView):
    template_name = 'shop/about.html'

class ContactView(FormView):
    template_name = 'shop/contact.html'
    form_class = ContactForm
    success_url = '/contact/'  # Redirect to the same contact page or wherever you want

    def form_valid(self, form):
        # Save the data to the Contact model
        contact = Contact(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            phone=form.cleaned_data['phone'],
            desc=form.cleaned_data['message']
        )
        contact.save()
        return super().form_valid(form)

class TrackerView(TemplateView):
    template_name = 'shop/tracker.html'

class SearchView(View):
    def get(self, request):
        return HttpResponse("we are at search")

class ProductView(DetailView):
    model = Product
    template_name = 'shop/product.html'
    context_object_name = 'product'

    def get_object(self):
        myid = self.kwargs.get("myid")
        return get_object_or_404(Product, id=myid)
    
    def post(self, request, *args, **kwargs):

        product = self.get_object()
        return redirect('add_to_cart', myid=product.id)

class CheckoutView(TemplateView):
    template_name = 'shop/checkout.html'
    
    
@csrf_exempt 
def submit_data(request):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        myid=int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=myid)
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity =quantity
            cart_item.save()
        return JsonResponse({'message': 'Data received successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

    