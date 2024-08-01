# views.py
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, TemplateView, DetailView, FormView, View
from django.views.decorators.http import require_POST
from django.http import HttpResponse,JsonResponse
from .models import *
from .forms import ContactForm
from math import ceil
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class IndexView(LoginRequiredMixin,ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'allProds'
    login_url = '/shop/login/'
    redirect_field_name = 'redirect_to'

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
    success_url = reverse_lazy('thanks') 

    def form_valid(self, form):
        # Save the data to the Contact model
        contact = Contact(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            phone=form.cleaned_data['phone'],
            desc=form.cleaned_data['message']
        )
        contact.save()
        return redirect('thanks/')


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
    
    
@csrf_protect
@login_required
def submit_data(request):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        myid=int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=myid)
        user = request.user
        cart_item ,created= Cart.objects.get_or_create(user=user, product=product)
        print(quantity)
        cart_item.quantity = quantity
        cart_item.save()
        return JsonResponse({'message': 'Data received successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

@login_required
@require_POST
def update_cart(request):
    try:
        action = request.POST.get('action')
        product_id = request.POST.get('product_id')
        if not product_id:
            return JsonResponse({'success': False, 'message': 'Product ID not provided.'})

        cart_item = get_object_or_404(Cart, product__id=product_id, user=request.user)

        if action == 'delete':
            cart_item.delete()
            return JsonResponse({'success': True, 'message': 'Item deleted successfully.'})

        elif action == 'update':
            quantity = request.POST.get('quantity')
            if not quantity or int(quantity) < 1:
                return JsonResponse({'success': False, 'message': 'Invalid quantity.'})
            cart_item.quantity = int(quantity)
            cart_item.save()
            return JsonResponse({'success': True, 'message': 'Quantity updated successfully.'})

        return JsonResponse({'success': False, 'message': 'Invalid action.'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})



class ThanksView(TemplateView):
    template_name = 'shop/thanks.html'
    

class CartItems(ListView):
    model = Cart
    template_name = 'shop/cartitems.html'
    context_object_name = 'cart_items'


    def get_queryset(self):
        return Cart.objects.all()


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/shop')
    else:
        form = CustomUserCreationForm()
    return render(request, 'shop/signup.html', {'form': form})

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'shop/login.html'
    success_url = reverse_lazy('index')

    
